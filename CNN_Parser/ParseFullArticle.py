import bs4
import datetime
from CNN_Parser.NewsArticle import NewsArticle

# https://stackoverflow.com/questions/14257717/python-beautifulsoup-wildcard-attribute-id-search
#sections = soup.find_all("tr", {"id" : lambda L: L and L.startswith('uid')})

'''
cnn.com
Has a section of metadata like follows.
<meta content="app-news-section" itemprop="articleSection"/>
<meta content="2018-02-09T18:27:47Z" itemprop="dateCreated"/>
<meta content="2018-02-09T18:27:47Z" itemprop="datePublished"/>
<meta content="2018-02-09T18:27:47Z" itemprop="dateModified"/>
<meta content="https://www.cnn.com/2018/02/09/app-news-section/what-happened-this-week-in-anything-but-politics-trnd/index.html" itemprop="url"/>
<meta content="Ana Johnson" itemprop="author"/>
<meta content="What happened this week (in anything but politics) - CNN" itemprop="headline"/>
<meta content="A rocket takes off. A mom storm off. And eggs fly off. It's time for this week's politics-free side of the news. " itemprop="description"/>
<meta content="app-news-section, What happened this week (in anything but politics) - CNN" itemprop="keywords"/>
<meta content="https://cdn.cnn.com/cnnnext/dam/assets/180207150425-gerber-2018-spokesbaby-super-tease.jpg" itemprop="image"/>
<meta content="https://cdn.cnn.com/cnnnext/dam/assets/180207150425-gerber-2018-spokesbaby-super-tease.jpg" itemprop="thumbnailUrl"/>
<meta content="What happened this week (in anything but politics)" itemprop="alternativeHeadline"/>
'''

def ParseFullArticle(soup):
    # CNN has two types of html that change depending on the URL:
    baseObj = ParseFullArticleCNNBase(soup)
    moneyObj = ParseFullArticleMoney(soup)
    if  baseObj.article_title is not None:
        return baseObj
    else:
        return moneyObj

def ParseFullArticleCNNBase(soup):
    author_soup = soup.find("meta", {"itemprop": "author"})
    date_published_soup = soup.find("meta", {"itemprop": "datePublished"})
    headline_soup = soup.find("meta", {"itemprop": "headline"})
    url_soup = soup.find("meta", {"itemprop": "url"})

    author = author_soup["content"] if (author_soup is not None) else None
    date = date_published_soup["content"] if (date_published_soup is not None) else None
    headline = headline_soup["content"] if (headline_soup is not None) else None
    url = url_soup["content"] if (url_soup is not None) else None

    # print("author: " + str(author))
    # print("date: " + str(date))
    # print("headline: " + str(headline))
    # print("url: " + str(url))

    text_list = list()
    for text_soup in soup.find_all("div", {"class": lambda x: x and "zn-body__paragraph" in x}):
        text_list.append(text_soup.get_text())
        text_list.append("\n")

    full_text = ''.join(text_list)
    return create_news_article_obj(article_title=headline, date=date, url=url, author=author, article_text=full_text)


def ParseFullArticleMoney(soup):
    author_soup = soup.find("meta", {"name": "author"})
    date_published_soup = soup.find("meta", {"name": "date"})
    headline_soup = soup.find("meta", {"name": "title"})
    url_soup = soup.find("meta", {"property": "og:url"})

    author = author_soup["content"] if (author_soup is not None) else None
    date = date_published_soup["content"] if (date_published_soup is not None) else None
    headline = headline_soup["content"] if (headline_soup is not None) else None
    url = url_soup["content"] if (url_soup is not None) else None

    # print("author: " + str(author))
    # print("date: " + str(date))
    # print("headline: " + str(headline))
    # print("url: " + str(url))

    text_soup = soup.find("div", {"id":"storytext"})
    text_list = list()
    for text in text_soup.find_all("p"):
        text_list.append(text.get_text())
        text_list.append("\n")

    full_text = ''.join(text_list)
    return create_news_article_obj(article_title=headline, date=date, url=url, author=author, article_text=full_text )


def create_news_article_obj(article_title=None, tags=None, date=None, url=None, author=None, article_text=None, image_descriptions=None):
    obj = NewsArticle()
    obj.article_title = article_title
    obj.tags = tags
    obj.date = date
    obj.url = url
    obj.author = author
    obj.article_text = article_text
    obj.image_descriptions=image_descriptions
    obj.source = "http://www.cnn.com/"
    return obj