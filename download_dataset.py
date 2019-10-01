import os

from google_drive_downloader import GoogleDriveDownloader as gdd


os.system("git clone git@github.com:xmodal-multilang-retrieval/flickr30k_entities.git ../flickr30k_entities")

gdd.download_file_from_google_drive(
    file_id='1Gbl0mgpCMOYFj7eRUUh4o4iX9t-mXTZv',
    dest_path='../flickr-image-dataset.zip',
    unzip=True,
    showsize=True,
)

os.system("mv ../flickr30k_images/ ../temp/")
os.system("mv ../temp/flickr30k_images/ ../")
os.system("rm -rf ../temp/")
os.system("rm ../flickr-image-dataset.zip")
