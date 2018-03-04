class NewsArticle:
    '''
    News Article Object:
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

    article_title = None
    tags = list()
    date = None
    source = None
    url = None
    author = None
    article_text = None
    image_descriptions = None

    def __str__(self):
        output_str = ""
        output_str += "Headline: " + str(self.article_title) + "\n"
        output_str += "Date: " + str(self.date) + "\n"
        output_str += "Article Text: " + str(self.article_text) + "\n"
        output_str += "Tags: " + str(self.tags) + "\n"
        output_str += "Image Descriptions: " + str(self.image_descriptions) + "\n"
        output_str += "Source: " + str(self.source) + "\n"
        output_str += "Link: " + str(self.url) + "\n"
        return output_str

