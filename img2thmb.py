from PIL import Image
import os

#archive_path = os.path.abspath(r"/home/matthew/pic_archive/2025/DSC05946.JPG")
#img_path = os.path.
archive_path = r"/home/matthew/pic_archive"
img_path = r"2025/DSC05946.JPG"

print(os.path.join(archive_path, img_path))

img = Image.open(os.path.join(archive_path, img_path))
thmb_size = (100,100)
img.thumbnail(thmb_size)

thmb_path = r"thmb_2025/DSC05946.JPG"
img.save(os.path.join(archive_path, thmb_path))