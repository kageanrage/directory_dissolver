import sys
import os
from config import Config
from send2trash import send2trash

cfg = Config()
test_mode = False

# Directory Dissolver
# use batch file to specify directory (dir)
# script will delete all sub-dirs of that dir, moving any files contained within the sub-dirs, to that dir


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
    print('{} is the direc'.format(direc))
    return direc


directory = tell_me_which_directory()
print(f'Directory = {directory}\n')
os.chdir(directory)  # change cwd to the desired directory
root_dir = os.path.abspath('.')  # define root_dir in absolute terms
for folderName, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        old_name = os.path.join(folderName, filename)
        new_name = os.path.join(root_dir, filename)
        print(f"{old_name}       <- WILL MOVE or RENAME TO: \n{new_name}\n")
        if not test_mode:
            try:
                os.rename(old_name, new_name)
            except FileExistsError:
                print(f'Duplicate filename so deleting a copy: {old_name}')
                send2trash(old_name)

for folderName, subfolders, filenames in os.walk(directory):
    for subfolder in subfolders:
        full_folder_path = os.path.join(folderName, subfolder)
        print(f'{full_folder_path}   <- Folder to be deleted')
        if not test_mode:
            send2trash(full_folder_path)
