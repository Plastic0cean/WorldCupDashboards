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
        return conn.execute(f"SELECT * FROM PlayerGoalsByTeam ({player_id}) ORDER BY number_of_goals DESC", True)