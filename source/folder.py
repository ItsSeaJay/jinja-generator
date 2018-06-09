import os
import shutil

"""Clears the contents of the specified folder"""
def clear(folder):
    # Iterate through every item in the folder,
    # and none of the ones beneath it
    for item in os.listdir(folder):
        # Create a valid system path using the specified folder
        # and current item
        path = os.path.join(folder, item)

        # Attempt to discern whether the item is a file or a folder
        # and delete that item
        try:
            if os.path.isfile(path):
                os.unlink(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        except Exception as e:
            print(e)

def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        print('Directory not copied. Error: %s' % e)

def copy_list(src, dest):
    file_list = os.listdir(src)

    for file_name in file_list:
        full_name = os.path.join(src, file_name)

        if (os.path.isfile(full_name)):
            shutil.copy(full_name, dest)
