from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Table, MetaData

from NewsArticle import NewsArticle

#from ESPN2 import crawlFrontPage as espn_arts
from Reddit import newsHeadlines as reddit_arts
from HackerNews import Search as hacker_arts
from BBC_Parser import Search as bbc_arts

engine = create_engine(
    'mysql+mysqlconnector://UIUC.ADSA:uiucadsa123@adsascrape.cqnah55gg5pq.us-east-1.rds.amazonaws.com:3306/adsawebscrape')

Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData(engine, reflect=True)

# Creates the NewsArticles table
if len(metadata.tables) == 0:
    Table('NewsArticles', metadata,
          Column('article_id', Integer, primary_key=True),
          Column('title', VARCHAR(200), index=True),
          Column('source', VARCHAR(50), index=True),
          Column('url', VARCHAR(length=2083)),
          Column('author', VARCHAR(50), index=True),
          Column('text', VARCHAR(6000))).create()

#session.add_all(Articles.scrape_new_articles())
session.commit()
class Articles:

    #To-Do: Filter out non natural language characters
    @staticmethod
    def scrape_new_articles():
        #new_articles.append(espn_arts.return_front_espn_headlines())
        r = reddit_arts.get_homepage_articles()
        h = hacker_arts.get_homepage_articles()
        b = bbc_arts.get_homepage_articles()
        new_articles = r + h + b        
        return new_articles

    @staticmethod
    def update_table(articles):
        print("{} rows deleted".format(session.query(NewsArticle).delete()))
        session.commit()
        for art in articles:
            session.add(art)
        session.commit()

    @staticmethod
    def get_headlines_by_source(source):
        source=str(source).lower()
        headlines = []
        for headline in session.query(NewsArticle.title).\
            filter(NewsArticle.source==source):
            headlines.append(headline.title)
        return headlines

    @staticmethod
    def get_all_headlines():
        return session.query(NewsArticle.title)

def main():
    Articles.update_table(Articles.scrape_new_articles())
    # arts = Articles.get_headlines_by_source('Reddit')
    # for a in arts:
    #     print(a.title)

if __name__ == '__main__':
    main()
