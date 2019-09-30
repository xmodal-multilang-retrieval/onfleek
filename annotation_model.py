
from typing import List
from pathlib import Path

from mypy_extensions import TypedDict
from superjson import json


class Translation(TypedDict):
    markers: List[str]
    original_sentence: str
    translated_sentences: List[str]


def save_annotation(
    image_id: int,
    caption_id: int,
    original_sentence: str,
    translated_sentence: str,
    marker: str,
    folder: Path,
):
    obj = Translation(
        markers=[marker],
        original_sentence=original_sentence,
        translated_sentences=[translated_sentence],
    )
    translation_file: Path = folder / str(image_id) / f"{caption_id}.json"
    if translation_file.is_file():
        data = Translation(**json.load(str(translation_file), verbose=False))
        data["markers"].append(marker)
        data["translated_sentences"].append(translated_sentence)
        obj = data
    translation_file.parent.mkdir(parents=True, exist_ok=True)
    json.dump(obj, str(translation_file), indent=2, overwrite=True, verbose=False)
    print(f"Saved IMG_{image_id}-CAP_{caption_id}.")
    

def load_annotation(
    image_id: int,
    caption_id: int,
    folder: Path,
) -> Translation:
    translation_file: Path = folder / str(image_id) / f"{caption_id}.json"
    if translation_file.is_file():
        data = Translation(**json.load(str(translation_file), verbose=False))
        return zip(data["markers"], data["translated_sentences"])
    msg = f"No translation file found for ID IMG_{image_id}-CAP_{caption_id}."
    raise ValueError(msg)