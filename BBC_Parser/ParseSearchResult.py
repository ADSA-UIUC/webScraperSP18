import datetime
from NewsArticle import NewsArticle
from NewsSource import NewsSource
from interface import implements

class BBCNewsSource (implements(NewsSource)):

def get_homepage_articles(soup):
    homepage_headline_class_tag = "block-link__overlay-link"

    headlines = soup.find_all("a", {"class": homepage_headline_class_tag})

    articles = list()

    for i in range(20):
        result = headlines[i]
        news_article = NewsArticle()

        news_article.title = result.string.strip()
        news_article.url = result['href']
        news_article.source = "BBC"
        articles.append(news_article)
    return articles


# https://stackoverflow.com/questions/14257717/python-beautifulsoup-wildcard-attribute-id-search
#sections = soup.find_all("tr", {"id" : lambda L: L and L.startswith('uid')})
def get_search_result(soup):
    search_result_class_tag = "search-results"
    headlines_class_tag = "headline"
    footer_date_tag = "flags btm"
    date_class_tag = "display-date"

    search_results = soup.find("ol", {"class": search_result_class_tag}).find_all("li")

    articles = list()

    for result in search_results:
        news_article = NewsArticle()

        result = result.find("div")
        result_headline = result.find("h1", {"itemprop": headlines_class_tag})
        # date under tags: footer -> dl -> dd -> time
        result_date = result.find("footer").find("dl", {"class":footer_date_tag}).find("dd").find("time", {"class": date_class_tag})

        news_article.title = result_headline.find("a").string.strip()
        news_article.url = result_headline.find("a")['href']
        #TODO: put date in correct format
        news_article.date = result_date.string.strip()
        news_article.source = "BBC"

        articles.append(news_article)

    return articles

def get_datetime_object(soup):
    date_string = soup.string.strip().replace(",", "")
    return datetime.datetime.strptime(date_string, '%b %d %Y')

def make_date_string(datetime_object):
    return str('%02d' % datetime_object.month) + "/" + str('%02d' % datetime_object.day) + "/" + str(datetime_object.year)