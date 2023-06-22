from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class DbConfig:
    server: str  
    driver: str 
    database: str 

@dataclass
class Config:
    db: DbConfig
    searching_threshold: float

    @classmethod
    def from_ini_file(cls, file: str):
        config = ConfigParser()
        config.read(file)
        return cls(
            DbConfig(config["DATABASE"]["server"], config["DATABASE"]["driver"], config["DATABASE"]["database"]),
            float(config["SEARCHING"]["threshold"])
        )


config = Config.from_ini_file("config.ini")