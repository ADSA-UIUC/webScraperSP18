'''
Class containing static methods that scrape NewsArticle objects
from www.news-gazette.com

@author diproray
#TODO: Image Description Tags using Microsoft Cognitive Services API
'''
class TheNewsGazette:

    @staticmethod
    def return_articles():

        articles_list = []

        r = requests.get("http://www.news-gazette.com/")
        soup = BeautifulSoup(r.content,'html.parser')

        for headline_object in soup.find_all('h2', class_ = 'headline'):
            article_url = "http://www.news-gazette.com" + headline_object.a['href']
            article = TheNewsGazette.return_article(article_url)
            articles_list.append(article)


        for headline_object in soup.find_all('h3'):
            if (headline_object.find(class_ = "icon-story") != None):
                article_url = "http://www.news-gazette.com" + headline_object.find('a')['href']
                article = TheNewsGazette.return_article(article_url)
                articles_list.append(article)

        return articles_list

    @staticmethod
    def return_article(article_url):

        article = NewsArticle("The News Gazette")
        article.article_title = TheNewsGazette.return_article_headline(article_url)
        article.url = TheNewsGazette.return_article_url(article_url)
        article.date = TheNewsGazette.return_article_date(article_url)
        article.tags = TheNewsGazette.return_article_tags(article_url)
        article.author = TheNewsGazette.return_article_author(article_url)
        article.article_text = TheNewsGazette.return_article_text(article_url)
        
        return article

    @staticmethod
    def return_article_headline(article_url):

        r = requests.get(article_url)
        soup = BeautifulSoup(r.content,'html.parser')

        title_object = soup.find('h1', class_ = 'title');
        return title_object.string

    @staticmethod
    def return_article_url(article_url):
        return article_url

    @staticmethod
    def return_article_date(article_url):

        r = requests.get(article_url)
        soup = BeautifulSoup(r.content,'html.parser')

        date_and_time_object = soup.find(class_ = 'timestamp')
        date_string = date_and_time_object.string[6:15]
        date_values_string_list = date_string.split('/')

        mm = date_values_string_list[0].zfill(2)
        dd = date_values_string_list[1].zfill(2)
        yy = date_values_string_list[2][-2:].zfill(2)

        return (mm + "/" + dd + "/" + yy)

    @staticmethod
    def return_article_author(article_url):

        r = requests.get(article_url)
        soup = BeautifulSoup(r.content,'html.parser')
        author_name_object = soup.find(class_ = 'authors')
        author_name = author_name_object.string

        if (author_name is None):
            return None

        author_name_list = author_name.split()
        author_last_name = author_name_list[1]
        author_first_name = author_name_list[0]

        return (author_last_name, author_first_name)

    @staticmethod
    def return_article_tags(article_url):

        r = requests.get(article_url)
        soup = BeautifulSoup(r.content,'html.parser')

        list_of_tags_objects = soup.find_all(class_ = 'vocab-terms')
        tags = []

        for list_of_tags_object in list_of_tags_objects:
            tag_objects = list_of_tags_object.find_all('a')
            for tag_object in tag_objects:
                tags.append(tag_object.string)

        return tags

    @staticmethod
    def return_article_text(article_url):

        r = requests.get(article_url)
        soup = BeautifulSoup(r.content,'html.parser')

        text_objects = soup.find_all('p')

        article_text = ''
        for text in text_objects:
            if (text.string is not None and "Login" not in text.string and "Subscribe" not in text.string):
                    article_text += " " + text.string

        return (article_text)
