'''
Class modelling a newspaper article
@author diproray
'''
class NewsArticle:

    '''
    Object Specification:
    “article_title” (string)
    “tags” (list of strings)
    “date” (string “mm/dd/yyyy”)
    “source” (might just be hard coded because this is from one website)
    “url” (string)
    “author” (tuple (last, first) )
    “article_text” (string)
    “image_descriptions” (if available in format list of strings)
    “summary” (Leave as None for now)
    “popularity_value”  (Leave as None for now) - but consider how you would create it for your site
    '''

    def __init__(self, source_name):

        self.article_title = None
        self.tags = []
        self.date = None
        self.source = source_name
        self.url = None
        self.author = None
        self.article_text = None
        self.image_descriptions = None

    def __str__(self):

        output_str = ""

        output_str += "Headline: " + str(self.article_title) + "\n"
        output_str += "Date: " + str(self.date) + "\n"
        if (self.author is not None):
            output_str += "Author: " + (self.author[1]) + " " + (self.author[0]) +"\n"
        else:
            output_str += "Author: None" + "\n"
        output_str += "Article Text: " + str(self.article_text) + "\n"
        output_str += "Tags: " + str(self.tags) + "\n"
        output_str += "Image Descriptions: " + str(self.image_descriptions) + "\n"
        output_str += "Source: " + str(self.source) + "\n"
        output_str += "Link: " + str(self.url) + "\n"
        
        return output_str
