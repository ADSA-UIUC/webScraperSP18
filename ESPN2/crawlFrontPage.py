from bs4 import BeautifulSoup
import requests

from NewsArticle import NewsArticle


def __init__(self):
    pass


#does what it says
def return_front_espn_headlines():
    list_of_headlines = {}
    source = "https://espn.com"
    espn = requests.get(source).text
    soup = BeautifulSoup(espn, "html5lib")

    find_content = soup.find_all("div", class_ = "contentItem__contentWrapper")
    for tag in find_content:
        list_of_headlines.append(tag.h1.title)

    list_of_objects = {}
    for headline in list_of_headlines:
        temp = NewsArticle(headline,None,None,source,None,None,None,None)
        list_of_headlines.append(temp)

    return list_of_objects
