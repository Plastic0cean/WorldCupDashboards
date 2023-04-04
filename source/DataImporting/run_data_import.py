from Db.DbConnection import conn 
from . import DataLoader 
from . import FileReader
import os
from pathlib import Path


PATH = r"C:\Users\bania\source\repos\WorldCubDashboards\dataset\fromGithub"

for f in os.listdir(PATH):
    file = os.path.join(PATH, f)

    reader = FileReader.BatchCsvReader(file, ",", 100_000, quotechar='"')
    data_loader = DataLoader.DataLoader(reader.header, Path(file).stem, "NVARCHAR(4000)")
    data_loader.create_table(conn)

    
    for batch in reader.get_batch():
        data_loader.insert(conn, batch)
