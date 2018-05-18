from bs4 import BeautifulSoup
import requests

import sys
sys.path.append('..')
import NewsArticle
#does what it says
def return_front_espn_headlines():
    list_of_headlines = {}
    espn = requests.get("https://espn.com").text
    soup = BeautifulSoup(espn, "html5lib")

    find_content = soup.find_all("div", class_ = "contentItem__contentWrapper")
    for tag in find_content:
        list_of_headlines.append(tag.h1.title)

    list_of_objects = {}
    for headline in list_of_headlines:
        temp = NewsArticle()
        temp.title = headline
        temp.source = "ESPN"
        list_of_headlines.append(temp)

    return list_of_objects
