from Db.DbConnection import conn


def get_all_players_names():
    with conn:
        names = conn.execute("SELECT * FROM PlayersList() ORDER BY name ASC", True)
    return names


def get_player_by_id(player_id: str):
    query = f"SELECT * FROM GetPlayerById('{player_id}')"
    with conn:
        player = conn.execute(query, True)
    return player[0]


def get_player_goals_by_team(player_id: str):
    with conn:
        return conn.select_as_dict(
            f"SELECT * FROM PlayerGoalsByTeam ('{player_id}') ORDER BY number_of_goals DESC")
    

def get_player_awards(player_id: str):
    with conn:
        return conn.execute(f"SELECT * FROM PlayerAwards('{player_id}')", True)
    

def get_player_basic_stats(player_id: str):
    with conn:
        return conn.execute(f"SELECT * FROM PlayerBasicStatistics('{player_id}')", True)[0]
    

def get_matches_by_tournament(player_id: str):
    with conn:
        return conn.select_as_dict(
            f"SELECT * FROM PlayerApperancesByTournament('{player_id}')"
            )

def get_apperances_summary(player_id: str):
        with conn:
            return conn.execute(f"SELECT * FROM PlayerTournamentSummary('{player_id}')", True)


def get_number_of_matches(player_id: str):
        with conn:
            return conn.execute(f"SELECT * FROM PlayerNumberOfMatches('{player_id}')", True)[0]


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

