from PIL import Image
import os
from pillow_heif import register_heif_opener

register_heif_opener()


# Get the list of all files and directories
path = "<PATH_OF_SOURCE_DIRECTORY>"
destPath = "<PATH_OF_DESTIONATION_DIRECTORY>"
dir_list = os.listdir(path)
dest_dir_list = os.listdir(destPath)

length = len(dir_list)
count = 0
for image in dir_list:
    count += 1
    if (image in dest_dir_list):
        continue
    print("CONVERTING THE FILE: ", image)
    try:
        foo = Image.open(path + image)
        foo.save(destPath + image, optimize=True, quality=50)
    except OSError:
        im = Image.open(path + image)
        rgb_im = im.convert('RGB')
        rgb_im.save(path + image)
        foo = Image.open(path + image)
        foo.save(destPath + image, optimize=True, quality=50)
    print(f"COMPLETED: {count}/{length}")
