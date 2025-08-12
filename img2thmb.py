# A script to take images and convert them to thumbnails
# 
from PIL import Image
import os
import argparse
import sys

# year: str of the folder name (a year)
def generate_thumbnails(year, size):
    thumb_size = (size, size)
    image_year_dir = os.path.join("images", year)
    thumb_year_dir = os.path.join("thumbnails", year)
    try:
        os.mkdir(thumb_year_dir)
    except FileExistsError:
        pass

    try:
        for file in os.listdir(image_year_dir):
            # file example: "/home/matthew/pic_archive/images/2025/DSC05986.JPG"
            image_full_path = os.path.join(image_year_dir, file)
            if not os.path.isfile(image_full_path):
                continue
            
            img = Image.open(image_full_path)
            img.thumbnail(thumb_size)
            thumb_full_path = os.path.join(thumb_year_dir, file)
            img.save(thumb_full_path)
    except FileNotFoundError:
        print(f"Specified image folder '{image_year_dir}' does not exist")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("year", help="the year of images to create thumbnails of")
    parser.add_argument("size", type=int, help="size of the thumbnail (square)",
                        default=150)
    args = parser.parse_args()
    generate_thumbnails(args.year, args.size)
    print(args.year + " done")