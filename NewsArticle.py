
class NewsArticle:
	#The title of the article
	title = ""

	#The category tags on the article
	tags = []

	#The date the article was released (Or updated?)
	date = "" #Change this to a date object

	#The source of the article
	source = "" #May be unnecessary

	#Permanent link to the article
	url = ""

	#The author of the article as a tuple (last, first)
	author = ()

	#The text body of the article
	text = ""

	#A list of image descriptions - one entry per image
	image_desc = []

	#A summarized version of the article 
	summary = "" #To be completed later

	#A popularity ranking for the article. Decide what this means at a later date
	popularity_value = 0 #Ignore for now

	#Initializes standard parameters for the date object
	def __init__(self, aTitle = None, aTags = None, aDate = None, aSource = None,
				 aUrl = None, aAuthor = None, aText = None, aImage_desc = None):
		self.title = aTitle
		self.tags = aTags
		self.date = aDate
		self.source = aSource
		self.url = aUrl
		self.author = aAuthor
		self.text = aText
		self.image_desc = aImage_desc

	