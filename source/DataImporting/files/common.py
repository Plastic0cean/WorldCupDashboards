import pandas as pd
from enum import Enum
import sqlalchemy


class DataSource(Enum):

    AWARD_WINNERS = r"dataset/award_winners.csv"
    AWARDS = r"dataset/awards.csv"
    PLAYERS = r"dataset/players.csv"
    BOOKINGS = r"dataset/bookings.csv"
    GOALS = r"dataset/goals.csv"
    GROUP_STANDINGS = r"dataset/group_standings.csv"
    MATCHES = r"dataset/matches.csv"
    PLAYER_APPEARANCES = r"dataset/player_appearances.csv"
    QUALIFIED_TEAMS = r"dataset/qualified_teams.csv"
    SQUADS = r"dataset/squads.csv"
    SUBSTITUTIONS = r"dataset/substitutions.csv"
    TEAMS = r"dataset/teams.csv"
    TEAM_APPEARANCES = r"dataset/team_appearances.csv"
    TOURNAMENT_STANDINGS = r"dataset/tournament_standings.csv"
    TOURNAMENTS = r"dataset/tournaments.csv"
    

def create_connection():
    # TODO: Move variables to config
    user = 'root'
    password = '668604112Xd'
    host = '127.0.0.1'
    port = 3306
    database = 'worldcupstatistics'
    return sqlalchemy.create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))


def read_dataset(source: DataSource, *kwargs) -> pd.DataFrame:
    return pd.read_csv(source.value, *kwargs)

def delete_columns(df: pd.DataFrame, to_delete: list[str]) -> pd.DataFrame:
    return df.drop(columns=to_delete)

def rename_columns(df: pd.DataFrame, columns_mapping: dict[str, str]) -> pd.DataFrame:
    return df.rename(columns=columns_mapping)

def import_to_db(data: pd.DataFrame, table: str) -> None:
    engine = create_connection()
    with engine.connect() as conn:
        data.to_sql(table, conn, if_exists="append", index=False, chunksize=1)
        conn.commit()