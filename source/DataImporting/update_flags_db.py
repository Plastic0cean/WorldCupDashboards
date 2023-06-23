from Db.DbConnection import conn 
from .files_functions import get_files_in_directory, get_filename_from_path

path = r".\static\images\flags" #Can be moved to config file

def update_names_of_flag_img_in_db(path: str) -> None:
    files = get_files_in_directory(path)

    for file in files:
        with conn:
            file_name = get_filename_from_path(file)
            team_id = file_name.split(".")[0]
            conn.execute(f"""
            UPDATE [teams] SET [flag_img] = '{file_name}'
            WHERE [team_id] = '{team_id}'
            """)


if __name__ == "__main__":
    update_names_of_flag_img_in_db(path)