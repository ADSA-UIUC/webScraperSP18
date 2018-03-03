import datetime
class NewsArticleHeadline:
    '''
    News Article Headline Object:
    “article_title” (string)
    “date” (string “mm/dd/yyyy”)
    “source” (might just be hard coded because this is from one website)
    “url” (string)
    “headline_text”
    '''

    article_title = None
    date = None
    source = "https://www.cnn.com"
    url = None
    headline_text = None

    def __str__(self):
        output_str = ""
        output_str += "Headline: " + self.article_title + "\n"
        output_str += "Text: " + self.headline_text + "\n"
        output_str += "Date: " + self.date + "\n"
        output_str += "Link: " + self.url + "\n"
        return output_str

    def get_date_as_datetime(self):
        try:
            date_string = self.date.replace("/", " ")
            return datetime.datetime.strptime(date_string, '%m %d %Y')
        except ValueError:
            return None