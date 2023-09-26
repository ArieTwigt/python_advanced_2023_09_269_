import os

# check files and folders
files_folders = os.listdir()

folder_name = 'data'

if folder_name not in files_folders:
    os.mkdir(folder_name)