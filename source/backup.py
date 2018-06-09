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
