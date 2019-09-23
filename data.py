
from collections import defaultdict
from pathlib import Path
from typing import List, Set, Tuple

import torch
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


images_folder = Path("../flickr30k_images/")
entities_folder = Path("../flickr30k_entities/")


def read_file(file_path: Path) -> str:
    with open(file_path) as file_obj:
        return file_obj.read()


def read_table(serialized_table: str, delimiter: str, remove_header: bool = True) -> List[List[str]]:
    table = [
        line.split(delimiter)
        for line in serialized_table.split("\n")
    ]

    if table[-1] == [""]:
        table = table[:-1]

    if remove_header:
        return table[1:]
    
    return table


class Flickr30k(Dataset):
    """
    Flickr30k Entities <http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities/> Dataset.

    :param img_folder: directory where the images are located.
    ann_file (string): Path to annotation file.
    transform (callable, optional): A function/transform that takes in a PIL image
        and returns a transformed version. E.g, ``transforms.ToTensor``
    target_transform (callable, optional): A function/transform that takes in the
        target and transforms it.
    """

    def __init__(
        self,
        images_folder: Path = images_folder,
        annotations_folder: Path = entities_folder,
        split: str = "test",
        transforms=None,
        target_transforms=None,
    ):
        super().__init__()
        assert split in ("train", "val", "test")
        self.img_folder = images_folder
        self.transforms = transforms
        self.target_transforms = target_transforms

        split_instances: Set[str] = set(read_file(annotations_folder / f"{split}.txt").split("\n"))

        annotations_table = read_table(read_file(annotations_folder / "captions.csv"), "|")

        self.annotations = defaultdict(list)
        for image_name, _, caption in annotations_table:
            if image_name[:-4] in split_instances:
                self.annotations[image_name].append(caption)

        self.ids = sorted(self.annotations.keys())

    def __getitem__(self, index: int) -> Tuple[Image.Image, List[str]]:
        """

        :return: Tuple (image, target). target is a list of captions for the image.
        """
        img_id = self.ids[index]

        # Image
        filename = self.img_folder / img_id
        img = Image.open(filename).convert('RGB')
        if self.transforms is not None:
            img = self.transforms(img)

        # Captions
        target = self.annotations[img_id]
        if self.target_transforms is not None:
            target = self.target_transforms(target)

        return img, target

    def __len__(self):
        return len(self.ids)


if __name__ == "__main__":
    dataset = Flickr30k(images_folder, entities_folder, "val")
    for img, target in dataset:
        img.show()
        print(target)
        break

