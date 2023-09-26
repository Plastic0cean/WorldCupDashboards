from enum import Enum
import pandas as pd
import sqlalchemy
from Config import Config, config


class DataSource(Enum):

    AWARD_WINNERS = r"../dataset/award_winners.csv"
    AWARDS = r"../dataset/awards.csv"
    PLAYERS = r"../dataset/players.csv"
    BOOKINGS = r"../dataset/bookings.csv"
    GOALS = r"../dataset/goals.csv"
    GROUP_STANDINGS = r"../dataset/group_standings.csv"
    MATCHES = r"../dataset/matches.csv"
    PLAYER_APPEARANCES = r"../dataset/player_appearances.csv"
    QUALIFIED_TEAMS = r"../dataset/qualified_teams.csv"
    SQUADS = r"../dataset/squads.csv"
    SUBSTITUTIONS = r"../dataset/substitutions.csv"
    TEAMS = r"../dataset/teams.csv"
    TEAM_APPEARANCES = r"../dataset/team_appearances.csv"
    TOURNAMENT_STANDINGS = r"../dataset/tournament_standings.csv"
    TOURNAMENTS = r"../dataset/tournaments.csv"


def create_connection(config: Config):
    return sqlalchemy.create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            config.db.user, config.db.password, config.db.host, config.db.port, config.db.database))


def read_dataset(source: DataSource, *kwargs) -> pd.DataFrame:
    return pd.read_csv(source.value, *kwargs)


def delete_columns(df: pd.DataFrame, to_delete: list[str]) -> pd.DataFrame:
    return df.drop(columns=to_delete)


def rename_columns(df: pd.DataFrame, columns_mapping: dict[str, str]) -> pd.DataFrame:
    return df.rename(columns=columns_mapping)


def import_to_db(data: pd.DataFrame, table: str) -> None:
    engine = create_connection(config)
    with engine.connect() as conn:
        data.to_sql(table, conn, if_exists="append", index=False, chunksize=1000)
        conn.commit()