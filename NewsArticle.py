from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Table, MetaData

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

    @staticmethod
    def get_new_articles(self):
        pass

    @staticmethod
    def update_table(self):
        # session.bulk_save_objects(<list>)
        # session.commit()
        pass

    @staticmethod
    def get_articles_by_source(self):
        pass

    @staticmethod
    def get_all_articles(self):
        pass


Base.metadata.create_all(engine)
