import urllib.parse
import requests
import bs4
import sys
sys.path.append('..')
from NewsArticle import NewsArticle

from HackerNews.ParseSearchResult import *

'''
    Basc Information:
    1) This is a parser to parse a group of articles from CNN.com
    2) Parses articles via a group of filtering methods:
        a) Keywords
        b) Author
        c) Category
        d) ...
'''

'''
    # Had to install:
    1) beautiful soup 4
    2) urllib
'''
homepage_url = "https://news.ycombinator.com/"

# def main():
#     articles = get_homepage_articles(get_url_soup(homepage_url))
#     article_titles = []
#     for article in articles:
#         article_titles.append(article.title)
#     print(article_titles)
# if __name__ == '__main__':
#     main()

# # Takes:
# # search string
# # start_index article number to start at
# def create_url(search_string, page):
#     params = {}
#     params["q"] = search_string
#     params["page"] = page
#
#     return base_search_url + urllib.parse.urlencode(params)

def get_homepage_articles():
    return retrieve_homepage_articles(get_url_soup(homepage_url))

def get_url_soup(url, browser=None):
    if browser is None:
        html_doc = requests.get(url).text
        if len(html_doc) < 50:
            return None
        else:
            return bs4.BeautifulSoup(html_doc, "html.parser")
    else:
        # Selenium webdriver loads javascript data:
        # https://stackoverflow.com/questions/11047348/is-this-possible-to-load-the-page-after-the-javascript-execute-using-python
        browser.get(url)
        soup = bs4.BeautifulSoup(browser.page_source, "html.parser")
        return soup
