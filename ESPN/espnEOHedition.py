from bs4 import BeautifulSoup
import requests

espn_link = "http://espn.com"
espn = requests.get(espn_link).text
soup = BeautifulSoup(espn,"html5lib")
headline_list = list()

total_headlines = soup.find_all("h1",class_ = "contentItem__title contentItem__title--story")

for headline in total_headlines:
    headline_list.append(headline.string)

top_headline = soup.find_all("h1", class_ = "module_header")
print(len(top_headline))
for top in top_headline:
    print(len(top))
