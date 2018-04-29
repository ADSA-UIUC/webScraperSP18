from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Table, MetaData

from ESPN import crawlFrontPage as espn_arts
'''
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
'''
engine = create_engine(
    'mysql+mysqlconnector://UIUC.ADSA:uiucadsa123@adsascrape.cqnah55gg5pq.us-east-1.rds.amazonaws.com:3306/adsawebscrape')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

metadata = MetaData(engine, reflect=True)

# Creates the NewsArticles table
if len(metadata.tables) == 0:
    Table('NewsArticles', metadata,
          Column('article_id', Integer, primary_key=True),
          Column('title', VARCHAR(50), index=True),
          Column('source', VARCHAR(50), index=True),
          Column('url', VARCHAR(length=2083)),
          Column('author', VARCHAR(50), index=True),
          Column('text', VARCHAR(6000))).create()


class NewsArticle(Base):
    __tablename__ = 'NewsArticles'
    # Initializes standard parameters for the date object
    article_id = Column(Integer, primary_key=True)  # Leave blank this will auto-generate
    title = Column(VARCHAR(50), index=True)  # string - The title of the article
    source = Column(VARCHAR(50), index=True)  # string - The source of the article
    url = Column(VARCHAR(length=2083))  # string - Permanent link to the article
    author = Column(VARCHAR(50), index=True)  # string - The author of the article as a tuple (last, first)
    text = Column(VARCHAR(6000))  # string - The text body of the article


class Articles:
    @staticmethod
    def scrape_new_articles():
        return espn_arts.return_front_espn_headlines()

    @staticmethod
    def update_table():
    	arts = Articles.scrape_new_articles()
    	print(arts)
    	session.bulk_save_objects(arts)
    	session.commit()

    @staticmethod
    def get_articles_by_source():
        pass

    @staticmethod
    def get_all_articles():
        pass

Articles.update_table()
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