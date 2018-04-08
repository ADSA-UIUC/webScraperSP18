import bs4
import requests
import json
import datetime
import urllib.parse

#from NewsArticle import NewsArticle


def main():
    headlines = get_news_front_page_headlines()
    print(headlines)
    #NewsArticle.dumpArticles(headlines, "reddit")
    #headlines = NewsArticle.loadArticles("reddit")
    # for headline in headlines:
    #     print(headline)


def get_news_front_page_headlines(num_headlines=None):
    headlines = list()
    #url = "https://www.reddit.com/r/news/hot.json"
    url = "https://www.reddit.com/r/uiuc/hot.json"
    json_str = requests.get(url, headers = {'User-agent': 'your bot 0.2'}).text
    data = json.loads(json_str)
    for i in data["data"]["children"]:
        the_data = i["data"]
        if "title" in the_data.keys():
            #headlines.append(NewsArticle(the_data["title"]))
            headlines.append(the_data["title"])

    return headlines


if __name__ == '__main__':
    main()