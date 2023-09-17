from .ImageDownloader import ImageWebDownloader, ImageWebDownloadMenager
from repository.players import player_repository

directory = r"static\images\players"
players = player_repository.get_all()

for player in players:
    try:
        img = ImageWebDownloader(player.name, directory)
        img_downloader = ImageWebDownloadMenager(img)
        img_downloader.run_download(directory, player.player_id)
    except:
        print("Cannnot download picture of", player.name)
        continue
