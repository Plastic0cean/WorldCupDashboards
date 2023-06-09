from PIL import Image
import os 

def get_files_in_directory(path: str) -> list[str]:
    list_of_files = []
    for file in os.listdir(path):
        full_file_path = os.path.join(path, file)
        if os.path.isfile(full_file_path):
            list_of_files.append(full_file_path)
    return list_of_files

def get_filename_from_path(path: str) -> str:
    return os.path.basename(path)

def resize_image(file: str, size: tuple[int, int], new_directory: str) -> None:
    image = Image.open(file).convert('RGB')
    image.thumbnail(size, Image.LANCZOS)
    image.save(
        os.path.join(new_directory, os.path.basename(file)),
        'JPEG', 
        quality=88)