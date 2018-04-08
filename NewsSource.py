from interface import Interface

class NewsSource(Interface):

	# return NewsArticle objects for articles on homepage
    def getHomepageArticles(self):
        pass

   	# return NewsArticle objects for results of a keyword search 
    def getKeywordSearchArticles(self, keyword):
    	pass
    