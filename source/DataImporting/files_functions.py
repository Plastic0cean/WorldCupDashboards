from PIL import Image
import os 

def get_files_in_directory(path: str) -> list[str]:
    return [os.path.join(path, file) for file in os.listdir(path)]

def resize_image(file: str, size: tuple[int, int], new_directory: str) -> None:
    image = Image.open(file).convert('RGB')
    image.thumbnail(size, Image.LANCZOS)
    image.save(
        os.path.join(new_directory, os.path.basename(file)),
        'JPEG', 
        quality=88)