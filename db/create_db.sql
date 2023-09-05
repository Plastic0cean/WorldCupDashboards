CREATE TABLE award_winners (
	award_winners_id INT PRIMARY KEY,
	tournament_id VARCHAR(10),
	award_id VARCHAR(10),
	shared BOOLEAN,
	player_id VARCHAR(10)
);

CREATE TABLE awards (
	award_id VARCHAR(10) PRIMARY KEY,
	award_name VARCHAR(100),
	award_description VARCHAR(1000),
	year_introduced INT
);

CREATE TABLE bookings (
	booking_id VARCHAR(10) PRIMARY KEY,
	match_id VARCHAR(10),
	player_id VARCHAR(10),
	minute_regulation INT,
	minute_stoppage INT,
	yellow_card BOOLEAN,
	red_card BOOLEAN,
	second_yellow_card BOOLEAN,
	sending_off BOOLEAN
);

CREATE TABLE goals (
	goal_id VARCHAR(10) PRIMARY KEY,
	match_id VARCHAR(10),
	player_id VARCHAR(10),
	player_team_id VARCHAR(10),
	opponent_id VARCHAR(10),
	minute_regulation INT,
	minute_stoppage INT,
	match_period VARCHAR(100),
	own_goal BOOLEAN,
	penalty BOOLEAN
);

CREATE TABLE group_standings (
    group_standings_id INT AUTO_INCREMENT PRIMARY KEY,
	tournament_id VARCHAR(4000),
	stage_number int, 
	stage_name VARCHAR(4000),
	group_name VARCHAR(4000),
	position INT,
	team_id VARCHAR(4000),
	played INT,
	wins INT,
	draws INT,
	losses INT,
	goals_for INT ,
	goals_against INT,
	points INT,
	advanced INT
);

CREATE TABLE matches(
	match_id VARCHAR(10) PRIMARY KEY,
	tournament_id VARCHAR(10),
	match_date DATE,
	match_time VARCHAR(10),
	stadium_id VARCHAR(10),
	home_team_id VARCHAR(10),
	away_team_id VARCHAR(10),
	home_team_score INT,
	away_team_score INT,
	extra_time BOOLEAN,
	penalty_shootout BOOLEAN,
	home_team_score_penalties INT,
	away_team_score_penalties INT,
	home_team_win BOOLEAN,
	away_team_win BOOLEAN,
	draw BOOLEAN,
	stage_name VARCHAR(100)
);

CREATE TABLE player_appearances (
	player_appearances_id INT AUTO_INCREMENT PRIMARY KEY,
	match_id VARCHAR(10),
	player_id VARCHAR(10),
    team_id VARCHAR(10),
	position VARCHAR(100),
	starter BOOLEAN,
	substitute BOOLEAN,
	captain BOOLEAN,
    minutes_played INT,
	shirt_number INT,
	UNIQUE KEY (match_id, player_id)
);

CREATE TABLE players (
	player_id VARCHAR(10) PRIMARY KEY,
	family_name VARCHAR(4000),
	given_name VARCHAR(4000),
	birth_date DATE,
	position VARCHAR(100),
	nationality VARCHAR(1000),
	count_tournaments INT,
	team_id VARCHAR(10)
);

CREATE TABLE qualified_teams(
	qualified_teams_id INT AUTO_INCREMENT PRIMARY KEY,
	tournament_id VARCHAR(10),
	team_id VARCHAR(10),
	count_matches INT,
	performance VARCHAR(100)
);

CREATE TABLE squads (
	squad_id INT AUTO_INCREMENT PRIMARY KEY,
	tournament_id VARCHAR(10),
	player_id VARCHAR(10),
	team_id VARCHAR(10),
	position VARCHAR(100)
);

CREATE TABLE substitutions (
	substitution_id VARCHAR(10) PRIMARY KEY,
	tournament_id VARCHAR(4000),
	match_id VARCHAR(10),
	team_id VARCHAR(10),
	player_id VARCHAR(10),
	minute_label VARCHAR(10),
	minute_regulation INT,
	minute_stoppage INT,
	match_period VARCHAR(100),
	going_off BOOLEAN,
	coming_on BOOLEAN
);

CREATE TABLE team_appearances (
	team_appearance_id INT AUTO_INCREMENT PRIMARY KEY,
	tournament_id VARCHAR(10),
	match_id VARCHAR(10),
	team_id VARCHAR(10),
	opponent_id VARCHAR(10),
	home_team BOOLEAN,
	away_team BOOLEAN,
	win BOOLEAN, 
	lose BOOLEAN, 
	draw BOOLEAN,
	goals_for INT,
	goals_against INT
);

CREATE TABLE teams (
	team_id VARCHAR(10) PRIMARY KEY,
	team_name VARCHAR(1000),
	team_code VARCHAR(20),
	federation_name VARCHAR(1000),
	region_name VARCHAR(1000),
	confederation_name VARCHAR(1000),
	confederation_code VARCHAR(1000),
	flag_img varchar(200) 
); 

CREATE TABLE tournament_standings (
	tournament_standings_id INT AUTO_INCREMENT PRIMARY KEY,
	tournament_id VARCHAR(10),
	position INT,
	team_id VARCHAR(4000)
);

CREATE TABLE tournaments (
	tournament_id VARCHAR(10) PRIMARY KEY,
	tournament_name VARCHAR(1000),
	year INT,
	start_date DATE,
	end_date DATE,
	host_country VARCHAR(1000)
);