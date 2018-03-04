import bs4
import requests
import json
import datetime
import urllib.parse

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
    2) selenium https://stackoverflow.com/questions/18868743/how-to-install-selenium-webdriver-on-mac-os
        * also requires geckodriver: https://codeyarns.com/2016/10/18/selenium-error-on-geckodriver/
    3) urllib
'''

# http://money.cnn.com/author/kaya-yurieff/index.html
# https://www.cnn.com/profiles/alanna-petroff

base_search_url = "https://www.cnn.com/search/?"

def main():

    headlines = get_headlines()
    for headline in headlines:
        print(str(headline))


def get_headlines(num_headlines=None):
    url = "https://www.cnet.com/"
    soup = get_url_soup(url)
    #print(soup.prettify())
    counter = 0
    headlines = list()
    for headline_soup in soup.find_all("a",{"section": lambda x: x is not None and "pebble" in x}):
        h3_soup = headline_soup.find("h3")
        if h3_soup is None:
            continue
        counter += 1
        headlines.append(h3_soup.get_text().strip())
        if num_headlines is not None and counter >= num_headlines:
            break

    return headlines


def get_url_soup(url):
    html_doc = requests.get(url).text
    if len(html_doc) < 50:
        return None
    else:
        return bs4.BeautifulSoup(html_doc, "html.parser")

if __name__ == '__main__':
    main()