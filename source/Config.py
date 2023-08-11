from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class DbConfig:
    host: str
    user: str
    password: str
    database: str
    port: str


@dataclass
class Config:
    db: DbConfig
    searching_threshold: float

    @classmethod
    def from_ini_file(cls, file: str):
        config = ConfigParser()
        config.read(file)
        db = DbConfig(
            config["DATABASE"]["host"], 
            config["DATABASE"]["user"], 
            config["DATABASE"]["password"], 
            config["DATABASE"]["database"],
            config["DATABASE"]["port"])
        
        searching = float(config["SEARCHING"]["threshold"])
        return cls(db, searching)

config = Config.from_ini_file("config.ini")