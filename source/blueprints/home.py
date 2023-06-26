import random 
from flask import Blueprint, render_template

home = Blueprint("home", __name__)

def get_random_quote():
    quotes = [
        {"author": "Serge Schmemann", "words": "Soccer is a great game, and the rich variety of styles and passions that come with being truly global makes the World Cup a nonpareil event in the universe of competitive sport."},
        {"author": "Pele", "words": "The World Cup is a very important way to measure the good players, and the great ones. It is a test of a great player"},
        {"author": "Rio Ferdinand", "words": "Nobody wants to be associated with failing to qualify for the World Cup finals. I cannot imagine the shame of it."},
        {"author": "Lionel Messi", "words": "You have to show up in the World Cup, and in the World Cup anything can happen."},
        {"author": "David Seaman", "words": "I will never forget my first game for England at the World Cup, It was against Turkey… no I mean Tunisia."},
        {"author": "David Beckham", "words": "That goal in the 1998 World Cup changed me-not as a person, but as a player. People have looked at me differently ever since. It gave me confidence and now I feel I can achieve anything."},
        {"author": "Andrea Pirlo", "words": "I don't feel pressure. I don't give a toss about it. I spent the afternoon of Sunday, July 9, 2006 in Berlin sleeping and playing the PlayStation. In the evening, I went out and won the World Cup."},
        {"author": "Sunil Gavaskar", "words": "When I die, the last thing I want to see is the six that Dhoni hit in the 2011 World Cup final."},
        {"author": "Hope Solo", "words": "My life goes in four-year cycles. The World Cup is every four years and the Olympics are every four years."},
        {"author": "Michael Owen", "words": "There's nothing quite like a World Cup."},
        {"author": "Alan Hansen", "words": "The boy can do anything, but to be the star of the World Cup you have got to get to the final and win it!"}
    ]
    return random.choice(quotes)


@home.route("/")
@home.route("/home")
def home_page():
    quote = get_random_quote()
    print(quote)
    return render_template("home.html", quote=quote)