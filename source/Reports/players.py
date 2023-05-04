from Db.DbConnection import conn
from Db.DbTableFunction import DbTableFunction


def get_all_players_names():
    return DbTableFunction("PlayersList").select(conn, sort_by="name")
    

def get_player_by_id(player_id: str):
    return DbTableFunction("GetPlayerById", player_id).select(conn)[0]


def get_player_goals_by_team(player_id: str):
    return DbTableFunction("PlayerGoalsByTeam", player_id).select_as_dict(conn, sort_by="number_of_goals")
    

def get_player_awards(player_id: str):
    return DbTableFunction("PlayerAwards", player_id).select(conn)
    

def get_player_basic_stats(player_id: str):
    return DbTableFunction("PlayerBasicStatistics", player_id).select(conn)[0]


def get_matches_by_tournament(player_id: str):
    return DbTableFunction("PlayerApperancesByTournament", player_id).select_as_dict(conn)


def get_apperances_summary(player_id: str):
    return DbTableFunction("PlayerTournamentSummary", player_id).select(conn)


def get_number_of_matches(player_id: str):
    return DbTableFunction("PlayerNumberOfMatches", player_id).select(conn)[0]


def get_minutes_played(player_id: str):
     with conn:
        query = f"""
        SELECT 
	    SUM(minutes_played) AS minutes_played,
	    SUM(possible_minutes - minutes_played) AS minutes_on_bench
        FROM PlayerMinutesPlayedByMatches('{player_id}')
        """
        return conn.select_as_dict(query)


def get_number_of_games_as_starter(player_id):
    with conn:
        query = f"""
            SELECT 
                SUM(CAST(starter AS INT)) AS starter,
                SUM(CAST(substitute AS INT)) AS substitute
            FROM player_appearances 
        WHERE player_id = '{player_id}'
        """
        result = conn.execute(query, True)
    
    return {
        "starer_or_sub": ["starter", "substitute"],
        "number_of_matches": [result[0].starter, result[0].substitute]
    }

