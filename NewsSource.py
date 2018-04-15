# https://pypi.python.org/pypi/python-interface/1.2.0
from interface import Interface

class NewsSource(Interface):

	# return NewsArticle objects for articles on homepage
    def get_homepage_articles(self):
        pass

   	# return NewsArticle objects for results of a keyword search 
    def get_keyword_search_articles(self, keyword):
    	pass  