import imghdr
import os

path = "<PATH_OF_DIRECTORY_OF_NO_EXTENSION_FILES>"
dir_list = os.listdir(path)

length = len(dir_list)
count = 0


# To add extensions
# for image in dir_list:
#     oldPath = path + image
#     ext = imghdr.what(oldPath);
#     if type(ext) == type(None):
#         ext = "jpg"
#     newPath = oldPath + "." + ext;
#     os.rename(oldPath, newPath)


# To remove extensions
# for image in dir_list:
#     oldPath = path + image
#     newPath = oldPath.split(".")[0]
#     # print(newPath)
#     os.rename(oldPath, newPath)