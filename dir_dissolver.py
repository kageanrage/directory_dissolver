import sys
import os
from config import Config
import send2trash

cfg = Config()
test_mode = False


def tell_me_which_directory():
    if len(sys.argv) > 1:
        direc = str(sys.argv[1])  # takes the desired directory from the command line argument, passed by the batch file
    else:
        if os.path.exists(r"C:\Program Files\StableBit\DrivePool"):
            print("Kev's Home PC detected, setting default test directory accordingly\n")
            direc = cfg.desktop_dir   # note this this the hardcoded directory for when working on Home PC
        else:
            print("This isn't Kev's Home PC, must be laptop, so setting test default directory accordingly\n")
            direc = cfg.laptop_dir
    return direc


def main_fn():
    directory = tell_me_which_directory()
    print('Directory = {}\n'.format(directory))
    os.chdir(directory) # change cwd to the desired directory
    abspath = os.path.abspath('.')  # define abspath
    for folderName, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            old_name = os.path.join(folderName, filename)
            new_name = os.path.join(abspath, filename)
            # print("{}       <- WILL MOVE TO: \n{}\n".format(old_name, new_name))
            if not test_mode:
                os.rename(old_name, new_name)
    for folderName, subfolders, filenames in os.walk(directory):
        for subfolder in subfolders:
            full_folder_path = os.path.join(folderName, subfolder)
            print('{}   <- Folder to be deleted'.format(full_folder_path))
            if not test_mode:
                send2trash.send2trash(full_folder_path)

main_fn()
