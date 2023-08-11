import random 
from flask import Blueprint, render_template

home = Blueprint("home", __name__)

def get_random_quote():
    quotes = [
        {"author": "Serge Schmemann", "words": "Soccer is a great game, and the rich variety of styles and passions that come with being truly global makes the World Cup a nonpareil event in the universe of competitive sport."},
        {"author": "Pele", "words": "The World Cup is a very important way to measure the good players, and the great ones. It is a test of a great player"},
        {"author": "David Seaman", "words": "I will never forget my first game for England at the World Cup, It was against Turkey… no I mean Tunisia."},
        {"author": "David Beckham", "words": "That goal in the 1998 World Cup changed me-not as a person, but as a player. People have looked at me differently ever since. It gave me confidence and now I feel I can achieve anything."},
        {"author":"Pelé", "words": "The more difficult the victory, the greater the happiness in winning."},
        {"author":"Denis Bergkamp", "words": "Behind every kick of a ball, there has to be a thought."},
        {"author":"Ronaldinho", "words":"Football is not just a game, it's an art form. You have to be creative, think outside the box, and always be one step ahead of your opponent."},
        {"author":"Diego Maradona", "words": "The game of football is like a canvas, and it's up to the players to paint the most beautiful picture."},
        {"author": "Arsene Wenger", "words":"Football is an art, like dancing is an art - but only when it's well done does it become an art."},
        {"author": "Didier Drogba", "words": "Football is more than just a game. It can bring hope and joy to people's lives."},
        {"author": "Bill Shankly", "words": "Some people think football is a matter of life and death. I assure you, it's much more serious than that."},
        {"author": "Nelson Falcão Rodrigues", "words": "In football, the worst blindness is only seeing the ball."},
        {"author": "Yaya Touré", "words": "I think football is more than a game, it is a passion. It is something that comes from inside and touches people's hearts."}
    ]
    return random.choice(quotes)


@home.route("/")
@home.route("/home")
def home_page():
    quote = get_random_quote()
    return render_template("home.html", quote=quote)