from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class DbConfig:
    server: str  
    driver: str 
    database: str 

    @classmethod
    def from_ini_file(cls, file: str):
        config = ConfigParser()
        config.read(file)
        return cls(
            config["DATABASE"]["server"],
            config["DATABASE"]["driver"],
            config["DATABASE"]["database"])


@dataclass
class Config:
    db: DbConfig




db_config = DbConfig.from_ini_file("config.ini")
config = Config(db_config)