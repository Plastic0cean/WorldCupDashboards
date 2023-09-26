import os 
import shutil
from bing_image_downloader import downloader


class ImageWebDownloader:

    def __init__(self, searched: str, output_directory: str) -> None:
        self.searched = searched
        self.output_directory = output_directory

    @property
    def result_directory(self) -> str:
        return os.path.join(self.output_directory, self.searched)

    @property
    def downloaded_images(self) -> list[str]:
        return [os.path.join(self.result_directory, file) for file in os.listdir(self.result_directory)]
    
    def download(self, how_many: int=1, adult_filter: bool=True, replace: bool=False, timeout: int=60) -> None:
        downloader.download(
            self.searched, 
            limit=how_many,
            output_dir=self.output_directory,
            adult_filter_off=adult_filter, 
            force_replace=replace, 
            timeout=timeout, 
            verbose=False)
        

class ImageWebDownloadMenager:

    def __init__(self, downloader: ImageWebDownloader) -> None:
        self.downloader = downloader

    def download_images(self):
        self.downloader.download()

    def move_downloaded_images(self, new_directory: str) -> None:
        for image in self.downloader.downloaded_images:
            shutil.move(image, os.path.join(new_directory, os.path.basename(image)))

    def delete_temp_directories(self) -> None:
        shutil.rmtree(self.downloader.result_directory)

    def rename_files(self, new_name: str) -> None:
        for index, file in enumerate(self.downloader.downloaded_images, 0):
            extention = os.path.splitext(file)[1]
            file_index = str(index) if index else ""
            os.rename(
                file, 
                os.path.join(self.downloader.result_directory, new_name + file_index + extention))

    def run_download(self, directory: str, files_result_name: str) -> None:
        self.download_images()
        self.rename_files(files_result_name)
        self.move_downloaded_images(directory)
        self.delete_temp_directories()
