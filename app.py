from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# quotes
quotes = [
	"Okay, wait, if we were one of Europe’s greatest leaders, and we were stranded in San Dimas for one day, where would we go?",
	"This is a dude who, 700 years ago, totally ravaged China, and who, we were told, 2 hours ago, totally ravaged Oshman’s Sporting Goods.",
	"Be excellent to each other!",
	"It seems to me the only thing you’ve learned is that Caesar is a 'salad dressing dude'.",
	"All we are is dust in the wind, dude.",
	"Strange things are afoot at the Circle-K.",
	"We're in danger of flunking most heinously tomorrow, Ted.",
	"Party on dudes!!",
	"Excellent!",
        "Iron Maiden? Excellent!",
        "Who was Joan of Arc? Noah's wife?!",
        "Shut up, Ted",
        "You know how to play, Rufus?",
        "I play a little...",
        "This is.. Dave Beeth-Oven... Maxine of Arc... Herman the Kid..., Bob Genghis Khan... So-crates Johnson... Dennis Freud. And uh... Abraham Lincoln...",
        "San Dimas High School football rules!",
        "That is why we need Eddie Van Halen!",
	"This has been a most excellent adventure."
]

@app.route("/")
def index():
	quote = random.choice(quotes)
	return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
