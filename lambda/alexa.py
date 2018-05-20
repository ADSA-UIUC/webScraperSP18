""" This is a flask app that handles alexa requests. This is ran after
installing 'flask-ask', 'cryptography<2.2', and 'ngrok' (this is not python).
This uses the simple templates in 'templates.yaml' and the alexa skill which
points to the 'ngrok' address. Run this python file and the ngrok program from
commandline to use the alexa service."""
import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_launch():
    welcome_msg = render_template("welcome")
    return question(welcome_msg)

@ask.intent("GiveMeTopHeadlines")
def get_headlines(NewsSource):
    # here you can put a function call instead of the hard coded list
    headlines = {
            "cnn": ["One", "two", "three"],
            "fox": ["uno", "dos", "tres"]
            }
    if NewsSource.lower() not in headlines:
        msg = render_template("sorry", name=NewsSource)
        return question(msg)
# or you could replace the 'headlines[NewsSource.lower()]' with a function call
    msg = render_template("headlines", name=NewsSource,\
            headlines=headlines[NewsSource.lower()])
    return question(msg)

if __name__=="__main__":
    app.run(debug=True)
