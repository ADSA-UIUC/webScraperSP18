'''
Class that has static functions which
scrape NewsArticle objects from https://thedailyillini.com

@author diproray
#TODO: Scrape image descriptions - possibly use Microsoft's Cognitive Services API
'''
class TheDailyIllini:

    @staticmethod
    def return_article_objects(number_of_headlines = 10):
        r = requests.get("https://dailyillini.com/")
        soup = BeautifulSoup(r.content,'html.parser')
        articles_list = []
        for headline_object, index in zip(soup.find_all(class_ = 'widgetheadline'), range(number_of_headlines)):
            article = TheDailyIllini.return_article(headline_object)
            articles_list.append(article)
        return articles_list

    @staticmethod
    def return_article(headline_object):
        article = NewsArticle("The Daily Illini")
        article.article_title = TheDailyIllini.return_article_headline(headline_object)
        article.url = TheDailyIllini.return_article_url(headline_object)
        article.date = TheDailyIllini.return_article_date(article.url)
        article.tags = TheDailyIllini.return_article_tags(article.url)
        article.author = TheDailyIllini.return_article_author(article.url)
        article.article_text = TheDailyIllini.return_article_text(article.url)
        return article

    @staticmethod
    def return_article_headline(headline_object):
        return headline_object.a.string

    @staticmethod
    def return_article_url(headline_object):
        return headline_object.a['href']

    @staticmethod
    def return_article_date(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser')
        date_string = soup.find(class_ = 'time-wrapper').string
        date_string = date_string.replace(",", "")
        date_string_list = date_string.split()
        mm_string = TimeParser.get_month_from_text(date_string_list[0])
        dd_string = date_string_list[1].zfill(2)
        yy_string = date_string_list[2][-2:]
        return mm_string + "/" + dd_string + "/" + yy_string

    @staticmethod
    def return_article_tags(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser').find(class_ = 'storycategory')
        tag_objects = soup.find_all('a')
        tags = []
        for tag_object in tag_objects:
            tags.append(tag_object.string)
        return tags

    @staticmethod
    def return_article_author(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser').find(class_ = 'storybyline')
        author_name = soup.a.string
        author_name_list = author_name.split()
        author_last_name = author_name_list[1]
        author_first_name = author_name_list[0]
        return (author_last_name, author_first_name)

    @staticmethod
    def return_article_text(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser').find(class_ = 'storycontent')
        text_objects = soup.find_all('p')
        article_text = ''
        for text in text_objects:
            if (text.string is not None and "the_content" not in text.string):
                    article_text += text.string
        return article_text
