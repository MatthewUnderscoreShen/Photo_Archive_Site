# A script to take images and convert them to thumbnails
# 
from PIL import Image
import os
import argparse

archive_path = r"/home/matthew/pic_archive"

# year: str of the folder name (a year)
def generate_thumbnails(year, size):
    thumb_size = (size, size)
    year_path = os.path.join(archive_path, "images", year)
    thumb_year = os.path.join(archive_path, "thumbnails", year)
    try:
        os.mkdir(thumb_year)
    except FileExistsError:
        pass
    
    for file in os.listdir(year_path):
        # file example: "/home/matthew/pic_archive/2025/DSC05986.JPG"
        full_path = os.path.join(year_path, file)
        if os.path.isfile(full_path):
            img = Image.open(full_path)
            img.thumbnail(thumb_size)
            thumb_path = os.path.join(thumb_year, os.path.basename(full_path))
            img.save(thumb_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("year", help="the year of images to create thumbnails of")
    parser.add_argument("size", type=int, help="size of the thumbnail (square)")
    args = parser.parse_args()
    generate_thumbnails(args.year, args.size)