from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'NewsArticles'
    # Initializes standard parameters for the date object
    article_id = Column(Integer, primary_key=True)  # Leave blank this will auto-generate
    title = Column(VARCHAR(200), index=True)  # string - The title of the article
    source = Column(VARCHAR(50), index=True)  # string - The source of the article
    url = Column(VARCHAR(length=2083))  # string - Permanent link to the article
    author = Column(VARCHAR(50), index=True)  # string - The author of the article as a tuple (last, first)
    text = Column(VARCHAR(6000))  # string - The text body of the article
