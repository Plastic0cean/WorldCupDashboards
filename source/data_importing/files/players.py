import pandas as pd
import numpy as np
import common

COLUMNS_TO_DELETE = [
    "key_id", "goal_keeper", "defender", 
    "midfielder", "forward", "player_wikipedia_link", 
    "list_tournaments"
    ]

def add_position(df: pd.DataFrame) -> pd.DataFrame:
    conditions = [df.goal_keeper == 1, df.defender == 1, df.midfielder == 1, df.forward == 1]
    values = ["goalkeeper", "defender", "midfielder", "forward"]
    df["position"] = np.select(conditions, values)
    return df

def add_nationality(players_df: pd.DataFrame) -> pd.DataFrame:
    pass

def clean_player_name(name: str) -> str:
    return None if name == "not applicable" else name

def clean_birth_date(date: str) -> str:
    return None if date == "not available" else date
    

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = add_position(df)
    df = common.delete_columns(df, COLUMNS_TO_DELETE)
    df["given_name"] = df["given_name"].apply(clean_player_name)
    df["birth_date"] = df["birth_date"].apply(clean_birth_date)
    return df

def process():
    players = common.read_dataset(common.DataSource.PLAYERS)
    players = transform(players)
    common.import_to_db(players, "players")

if __name__=="__main__":
    process()