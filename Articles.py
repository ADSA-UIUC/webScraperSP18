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

Articles.update_table()
