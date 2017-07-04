import sys
import os
from config import Config

cfg = Config()


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
    print('Directory = {}'.format(directory))
    os.chdir(directory) # change cwd to the desired directory
    abspath = os.path.abspath('.')  # define abspath
    for folderName, subfolder, filenames in os.walk(directory):
        print('folderName is {}'.format(folderName))
        print('subfolder is {}'.format(subfolder))
        print('filenames are {}'.format(filenames))
        for filename in filenames:
            print("Filename is {} but we'll make it {}".format())

        """
        original_basename, ext = os.path.splitext(filename) # isolate basename and extensions
        original_filename_incl_path = os.path.join(abspath, filename)  # original name incl path
        new_name_incl_path = os.path.join(abspath, new_name)    # new name incl path
        if not Test_mode:
            os.rename(original_filename_incl_path, new_name_incl_path)    # DISABLE FOR TESTING
        print('Renaming {} to {}'.format(original_filename_incl_path, new_name_incl_path))
        """

main_fn()
