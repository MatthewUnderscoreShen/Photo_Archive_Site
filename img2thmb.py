from PIL import Image
import os, glob

archive_path = r"/home/matthew/pic_archive"
years = ("2023", "2024", "2025")
thmb_size = (100,100)
for y in years:
    year_path = os.path.join(archive_path, y)
    thmb_year = "thmb" + y
    for file in glob.glob(os.path.join(year_path, "*.JPG")):
        # file example: "/home/matthew/pic_archive/2025/DSC05986.JPG"
        img = Image.open(file)
        img.thumbnail(thmb_size)
        thmb_path = os.path.join(archive_path, thmb_year, os.path.basename(file))
        img.save(thmb_path)