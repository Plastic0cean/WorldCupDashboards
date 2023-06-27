from flask import Flask, render_template
from blueprints.players import players 
from blueprints.teams import teams
from blueprints.tournaments import tournaments
from blueprints.matches import matches
from blueprints.home import home

app = Flask(__name__)
app.register_blueprint(players)
app.register_blueprint(teams)
app.register_blueprint(tournaments)
app.register_blueprint(matches)
app.register_blueprint(home)

if __name__ == "__main__":
    app.run(debug=True)