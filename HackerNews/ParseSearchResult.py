import datetime

from NewsArticle import NewsArticle

def retrieve_homepage_articles(soup):
    homepage_headline_class_tag = "storylink"

    headlines = soup.find_all("a", {"class": homepage_headline_class_tag})

    articles = list()

    for result in headlines:
        news_article = NewsArticle()

        news_article.title = result.string.strip()
        news_article.url = result['href']
        news_article.source = "HackerNews"
        articles.append(news_article)
    return articles


# https://stackoverflow.com/questions/14257717/python-beautifulsoup-wildcard-attribute-id-search
#sections = soup.find_all("tr", {"id" : lambda L: L and L.startswith('uid')})
def get_search_result(soup):
    pass
def get_datetime_object(soup):
    date_string = soup.string.strip().replace(",", "")
    return datetime.datetime.strptime(date_string, '%b %d %Y')

def make_date_string(datetime_object):
    return str('%02d' % datetime_object.month) + "/" + str('%02d' % datetime_object.day) + "/" + str(datetime_object.year)