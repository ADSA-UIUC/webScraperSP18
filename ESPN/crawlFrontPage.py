from bs4 import BeautifulSoup
import requests



def return_front_espn_headlines():
    list_of_headlines = {}
    source = "https://espn.com"
    espn = requests.get(source).text
    soup = BeautifulSoup(espn, "html5lib")

    find_content = soup.find_all("div", class_ = "contentItem__contentWrapper")
    for tag in find_content:
        list_of_headlines.append(tag.h1.title)
    return list_of_headlines
