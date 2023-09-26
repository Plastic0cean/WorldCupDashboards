from .ImageDownloader import ImageWebDownloader, ImageWebDownloadMenager
from repository.teams import team_repository

directory = r"static\images\flags"
teams = team_repository.get_all()

for team in teams:
    img = ImageWebDownloader(f"{team.team_name} flag", directory)
    img_downloader = ImageWebDownloadMenager(img)
    img_downloader.run_download(directory, team.team_id)
