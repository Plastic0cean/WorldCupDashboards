from .ImageDownloader import ImageWebDownloader, ImageWebDownloadMenager
from Reports.teams import get_all_team_names

directory = r"static\images\flags"
# query_string = "Poland flag"
# team_id = "T-55"

teams = get_all_team_names()
for team in teams:
    img = ImageWebDownloader(f"{team.team_name} flag", directory)
    img_downloader = ImageWebDownloadMenager(img)
    img_downloader.run_download(directory, team.team_id)
