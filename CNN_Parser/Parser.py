import bs4
import requests
import json
import datetime
import urllib.parse
from selenium import webdriver
import os
from CNN_Parser.ParseSearchResult import *
from CNN_Parser.NewsArticleHeadline import NewsArticleHeadline
from CNN_Parser.ParseFullArticle import *
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
    # Sets path used by selenium.
    # This will throw an error...
    os.environ["PATH"] = "/Users/alexandregeubelle/Desktop/Alexandre Geubelle/Coding/CNNParser"
    browser = webdriver.Firefox()

    get_headlines(10, browser=browser)
    # To get info on a full article:
    # url = "http://money.cnn.com/2018/03/01/technology/elon-musk-china-infrastructure-tweet/index.html"
    # soup = get_url_soup(url, browser=browser)
    # ParseFullArticle(soup)
    # print(str(ParseFullArticleMoney(soup)))

    # To get headlines between a certain time frame.
    #parse_headlines_by_search_term("Elon Musk", "03/02/2018", "01/01/2017", max_articles=15, browser=browser)

    # To get recent headlines
    # parse_recent_headlines_by_search_term("Elon Musk", 25, browser)) # Most recent 25 headlines.

    browser.quit()


def get_headlines(num_headlines=None, browser=None):
    url = "https://www.cnn.com/"
    soup = get_url_soup(url, browser=browser)
    counter = 0
    headlines = list()
    urls = list()
    for h3_soup in soup.find_all("h3",{"class": "cd__headline"}):
        counter += 1
        headlines.append(h3_soup.find("span", {"class":"cd__headline-text"}).get_text())
        url = h3_soup.find("a")["href"]
        if "https://www.cnn.com" not in url:
            url = "https://www.cnn.com" + url
        urls.append(url)
        if num_headlines is not None and counter >= num_headlines:
            break

    for i in range(len(urls)):
        print(str(urls[i]))
        print(str(headlines[i]))

    return headlines


def parse_recent_headlines_by_search_term(search_string, max_articles, browser=None):
    counter = 0
    all_headlines = list()
    while counter < max_articles and counter >= 0:
        end_index = counter + 100
        end_index = min(max_articles, end_index)
        num_articles = end_index - counter
        url = create_url(search_string=search_string, start_index=counter, num_articles=num_articles)
        soup = get_url_soup(url=url, browser=browser)
        if soup is not None:
            headlines = ParseSearchResult(soup)
            all_headlines.extend(headlines)
        counter += 100
    return all_headlines


def parse_headlines_by_search_term(search_string, start_date, end_date, max_articles = None, browser=None,):
    # Example url: https://www.cnn.com/search/?size=10&q=Trump&from=9900&type=article
    # https://www.cnn.com/search/?size=<ENTRIES_PER_PAGE>&q=<SEARCH_STRING>&from=<START_ENTRY>&type=article
    # cnn does not have searches by date, but you can order all results by date and binary search.
    start_date = start_date.replace("/", " ")
    end_date = end_date.replace("/", " ")
    recent_date_object = datetime.datetime.strptime(start_date, '%m %d %Y')
    old_date_object = datetime.datetime.strptime(end_date, '%m %d %Y')

    # print("Start: " + str(start_date_object))
    # print("End: " + str(end_date_object))

    base_url = create_url(search_string=search_string, start_index=0, num_articles=1)
    soup = get_url_soup(base_url, browser=browser)

    num_total_results = get_num_results(soup)
    print(num_total_results)

    # You can get the newest and oldest dates of a set of search results:
    # other_url = create_url(search_string=search_string, start_index=0, num_articles=100)
    # soup = get_url_soup(other_url, browser=browser)
    # date_ranges = get_range_of_dates(soup)

    counter = 0
    all_headlines = list()
    while counter < num_total_results and counter >= 0:
        end_index = counter + 100
        end_index = min(num_total_results, end_index)
        num_articles = end_index-counter
        url = create_url(search_string=search_string, start_index=counter, num_articles=num_articles)
        soup = get_url_soup(url=url, browser=browser)
        if soup is not None:
            headlines = ParseSearchResult(soup)
            for headline in headlines:
                headline_date = headline.get_date_as_datetime()
                if headline_date > recent_date_object: #The headline is from sooner the recent_date_object
                    continue
                elif headline_date < old_date_object: #The headline is from older than the old_date_object
                    counter = -1000 #Makes while loop exit as well.
                    break
                else:
                    all_headlines.append(headline)
                    if (max_articles is not None) and (len(all_headlines) >= max_articles):
                        counter = -1000  # Makes while loop exit as well.
                        break
        counter += 100

    return all_headlines


# Takes:
# search string
# start_index (Must not try and access an article greater than number 10,000)
# num_articles which must be (<100)
def create_url(search_string, start_index, num_articles):
    if  num_articles > 100 or (start_index + num_articles) > 10000:
        return None

    params = {}
    params["size"] = num_articles
    params["q"] = search_string
    params["from"] = start_index
    params["type"] = "article"
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