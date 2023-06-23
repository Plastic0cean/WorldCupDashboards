from flask import Flask, render_template
from blueprints.players import players 
from blueprints.teams import teams
from blueprints.tournaments import tournaments

app = Flask(__name__)
app.register_blueprint(players)
app.register_blueprint(teams)
app.register_blueprint(tournaments)

@app.route("/")
@app.route("/home")
def home():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)