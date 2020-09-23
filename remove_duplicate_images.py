import imagehash
from PIL import Image
from os import listdir, remove, rename
from collections import defaultdict


# This function removes the duplicate images and add the numbers
# of duplicate images to the front of the remaining images' file names
def remove_duplicate_images(directory_path):
    hash_to_file_names = defaultdict(list)
    for file_name in listdir(directory_path):
        if file_name.endswith('.jpg'):
            file_path = directory_path + file_name
            image = Image.open(file_path)
            phash = imagehash.phash(image)
            hash_to_file_names[phash].append(file_name)
    for file_names in hash_to_file_names.values():
        old_name = file_names[0]
        new_name = str(len(file_names)) + old_name
        old_path = directory_path + old_name
        new_path = directory_path + new_name
        rename(old_path, new_path)
        for file_name in file_names[1:]:
            file_path = directory_path + file_name
            remove(file_path)
            print('Removed')
    print('Done')