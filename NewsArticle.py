from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR
'''
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
'''

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'NewsArticles'
    # Initializes standard parameters for the date object
    article_id = Column(Integer, primary_key=True)  # Leave blank this will auto-generate
    title = Column(VARCHAR(50), index=True)  # string - The title of the article
    source = Column(VARCHAR(50), index=True)  # string - The source of the article
    url = Column(VARCHAR(length=2083))  # string - Permanent link to the article
    author = Column(VARCHAR(50), index=True)  # string - The author of the article as a tuple (last, first)
    text = Column(VARCHAR(6000))  # string - The text body of the article

'''
app = Flask(__name__)
ask = Ask(app, "/news")


@app.route('/')
def homepage():
    return "Hello"


@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like the news?'
    return question(welcome_message)


@ask.intent("YesIntent")
def share_headlines():
    headlines = NewsArticle.get_all_articles()
    headline_msg = 'The current world news headlines are {}'.format(headlines)
    return statement(headline_msg)


@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Okay... Bye.'
    return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
'''