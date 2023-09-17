import os 
from files_functions import resize_image, get_files_in_directory

SOURCE_PATH = r"C:\Users\bania\source\repos\WorldCubDashboards\source\static\images\flags"
RESULT_PATH = r"C:\Users\bania\source\repos\WorldCubDashboards\source\static\images\flags\150x150"
IMG_DIM = (150, 150)

files = get_files_in_directory(SOURCE_PATH)

for file in files:
    if os.path.isfile(file):
        resize_image(file, IMG_DIM, RESULT_PATH)