import common
import numpy as np
import pandas as pd

COLUMNS_TO_DELETE = [
    'key_id', 'tournament_id', 'tournament_name', 'match_name',
    'match_date', 'stage_name', 'group_name', 'team_name',
    'team_code', 'home_team', 'away_team', 'family_name',
    'given_name', 'shirt_number', 'position_code'
]

COLUMNS_MAPPING = {"position_name": "position"}

def find_players_subbed_twice(subs: pd.DataFrame) -> pd.Series:
    counts = subs.value_counts(["match_id", "player_id"])
    return counts[counts>1].reset_index()

def filter_repeated_substitutions(subs: pd.DataFrame) -> pd.DataFrame:
    subbed_twice = find_players_subbed_twice(subs)
    return subs[subs.player_id.isin(subbed_twice.player_id) & subs.match_id.isin(subbed_twice.match_id)]

def filter_not_repeated_substitutions(subs: pd.DataFrame) -> pd.DataFrame:
    subbed_twice = find_players_subbed_twice(subs)
    filtered = []
    for _, row in subs.iterrows():
        if subbed_twice[(subbed_twice.match_id == row.match_id) & (subbed_twice.player_id == row.player_id)].empty:
            filtered.append(row)
    return pd.DataFrame(filtered)

def process_repeated_substitutions(subs: pd.DataFrame):
    subs = filter_repeated_substitutions(subs)
    subs = subs.merge(subs, on=["player_id", "match_id"], suffixes=("", "_x"))
    subs = subs[["match_id", "player_id", "minute_regulation", "coming_on", "going_off", "minute_regulation_x", "coming_on_x", "going_off_x"]]
    subs = subs[subs["minute_regulation"] != subs["minute_regulation_x"]]
    conditions = [subs.coming_on == 1, subs.coming_on_x ==1]
    choices = [subs.minute_regulation, subs.minute_regulation_x]
    subs["ON"] = np.select(condlist=conditions, choicelist=choices)
    conditions = [subs.going_off == 1, subs.going_off_x ==1]
    choices = [subs.minute_regulation, subs.minute_regulation_x]
    subs["OFF"] = np.select(condlist=conditions, choicelist=choices)
    subs["minutes_played"] = subs["OFF"] - subs["ON"]
    subs = subs[["match_id", "player_id", "minutes_played"]]
    subs = subs.drop_duplicates()

def process_not_repeated_substitutions(player_apperances: pd.DataFrame, substitutions: pd.DataFrame, matches: pd.DataFrame):
    not_repeated_subs = filter_not_repeated_substitutions(substitutions)
    df = player_apperances.merge(matches, on="match_id").merge(not_repeated_subs, on=["player_id", "match_id"], how="left")
    df["possible_minutes"] = np.where(df.extra_time == 0, 90, 120)
    df["starter_minutes"] = np.where(np.isnan(df.minute_regulation), df.possible_minutes, df.minute_regulation)
    df["sub_minutes"] = df.possible_minutes - df.minute_regulation
    df["minutes_played"] = np.where(df.starter == 1, df.starter_minutes, df.sub_minutes).astype(int)
    df = df[["match_id", "player_id", "minutes_played"]]
    return df

def get_minutes_played(player_apperances: pd.DataFrame, substitutions: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    not_repeated = process_not_repeated_substitutions(player_apperances, substitutions, matches)
    repeated = process_repeated_substitutions(substitutions)
    result = pd.concat([not_repeated, repeated])
    result = result[result.minutes_played>=0]
    return result

def add_minutes_played(player_apperances: pd.DataFrame, substitutions: pd.DataFrame, matches: pd.DataFrame) -> pd.Series:
    minutes = get_minutes_played(player_apperances, substitutions, matches)
    return player_apperances.merge(minutes, on=["match_id", "player_id"])

def format_positions(df: pd.DataFrame) -> pd.DataFrame:
    mapping = {
        "center forward": "forward",
        "defender": "center back",
        "left forward": "left winger",
        "left midfielder": "left winger",
        "left wing back": "left winger",
        "midfielder": "center midfielder",
        "right forward": "right winger",
        "right midfielder": "right winger",
        "right wing back": "right winger",
        "second striker": "forward",
        "sweeper": "center back"
        }
    for to_replace, value in mapping.items():
        df.position = df.position.replace(to_replace, value)
    return df


def process():
    player_apperances = common.read_dataset(common.DataSource.PLAYER_APPEARANCES)
    substitutions = common.read_dataset(common.DataSource.SUBSTITUTIONS)
    matches = common.read_dataset(common.DataSource.MATCHES)

    player_apperances = add_minutes_played(player_apperances, substitutions, matches)
    player_apperances = common.delete_columns(player_apperances, COLUMNS_TO_DELETE)
    player_apperances = common.rename_columns(player_apperances, COLUMNS_MAPPING)
    player_apperances = format_positions(player_apperances)
    common.import_to_db(player_apperances, "player_appearances")


if __name__ == "__main__":
    process()