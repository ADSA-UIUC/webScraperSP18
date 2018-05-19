from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Table, MetaData

#from ESPN2 import crawlFrontPage as espn_arts
from Reddit import newsHeadlines as reddit_arts
__name__ = '__main__'
class Articles:
    @staticmethod
    def scrape_new_articles():
        #return espn_arts.return_front_espn_headlines()
        return reddit_arts.get_homepage_articles()

    @staticmethod
    def update_table():
        arts = Articles.scrape_new_articles()
        for a in arts:
            print(a.title)
    	#session.bulk_save_objects(arts)
    	#session.commit()

    @staticmethod
    def get_articles_by_source():
        pass

    @staticmethod
    def get_all_articles():
        pass

engine = create_engine(
    'mysql+mysqlconnector://UIUC.ADSA:uiucadsa123@adsascrape.cqnah55gg5pq.us-east-1.rds.amazonaws.com:3306/adsawebscrape')

Session = sessionmaker(bind=engine)
session = Session()

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

session.add_all(Articles.scrape_new_articles())
session.commit()

