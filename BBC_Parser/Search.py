import urllib.parse
import requests
import json
import datetime
import os
import bs4

from BBC_Parser.ParseSearchResult import *

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

# http://money.cnn.com/author/kaya-yurieff/index.html
# https://www.cnn.com/profiles/alanna-petroff

base_search_url = "https://www.bbc.co.uk/search?"

def main():
    url = create_url("elon musk", 2)
    articles = parse_search_result(get_url_soup(url))

# Takes:
# search string 
# start_index article number to start at
def create_url(search_string, page):
    params = {}
    params["q"] = search_string
    params["page"] = page

    return base_search_url + urllib.parse.urlencode(params)


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

if __name__ == '__main__':
    main()