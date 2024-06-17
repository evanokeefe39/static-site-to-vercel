import os

# in the ar_assets folder create sequentially named folders i.e image_1, image_2, image_3 etc
# this is to store the images that are downloaded from the web
def make_image_folders():
    # get the current working directory
    cwd = os.getcwd()

    # create the path to the ar_assets folder
    ar_assets_path = os.path.join(cwd, 'ar_assets')

    # create the image_folders folder
    os.makedirs(ar_assets_path, exist_ok=True)

    # create 100 image folders
    for i in range(1, 101):
        folder_name = 'image_' + str(i)
        folder_path = os.path.join(ar_assets_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    return

make_image_folders()