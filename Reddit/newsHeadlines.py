import bs4
import requests
import json
import datetime
import urllib.parse
import sys
sys.path.append('..')
from NewsArticle import NewsArticle

# class reddit_scraper:
#     def __init__(self):
#         pass


# return NewsArticle objects for articles on homepage
# BAILEY CALL THIS FUNCTION
def get_homepage_articles():
    headlines = list()
    subreddit = "all"
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    json_str = requests.get(url, headers = {'User-agent': 'your bot 0.2'}).text
    data = json.loads(json_str)
    for i in data["data"]["children"]:
        the_data = i["data"]
        if "title" in the_data.keys():
            new_article = NewsArticle(title=the_data["title"], source='Reddit')
            headlines.append(new_article)

    return headlines


# return NewsArticle objects for results of a keyword search 
def get_keyword_search_articles(keyword):
    pass

    # def main():
    #     url = "https://www.reddit.com/r/news/search?q=Trump&restrict_sr=on&sort=relevance&t=month"
    #     json_str = requests.get(url, headers = {'User-agent': 'your bot 0.2'}).text
    #     print(json_str)

    #     #headlines = get_news_front_page_headlines()
    #     #print(headlines)
    #     #NewsArticle.dumpArticles(headlines, "reddit")
    #     #headlines = NewsArticle.loadArticles("reddit")
    #     # for headline in headlines:
    #     #     print(headline)



# if __name__ == '__main__':
#     main()