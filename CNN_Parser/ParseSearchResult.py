import bs4
import datetime
from NewsArticleHeadline import NewsArticleHeadline

# https://stackoverflow.com/questions/14257717/python-beautifulsoup-wildcard-attribute-id-search
#sections = soup.find_all("tr", {"id" : lambda L: L and L.startswith('uid')})
def ParseSearchResult(soup):
    search_result_class_tag = "cnn-search__result-contents"
    headlines_class_tag = "cnn-search__result-headline"
    date_class_tag = "cnn-search__result-publish-date"
    text_body_class_tag = "cnn-search__result-body"

    search_results = soup.find_all("div", {"class": search_result_class_tag})

    headlines = list()

    for result in search_results:
        #print(result.prettify())
        headline = result.find("h3", {"class": headlines_class_tag})
        result_date = result.find("div", {"class": date_class_tag}).find("span", {"class": None})
        result_body = result.find("div", {"class": text_body_class_tag})

        url = headline.find("a")['href']
        headline_string = headline.find("a").string.strip()
        headline_text=  result_body.string.strip()
        date_time_string = make_date_string(get_datetime_object(result_date))

        headline_object = NewsArticleHeadline()
        headline_object.url = url
        headline_object.article_title = headline_string
        headline_object.headline_text = headline_text
        headline_object.date = date_time_string

        headlines.append(headline_object)

    return headlines

def get_range_of_dates(soup):
    search_result_class_tag = "cnn-search__result-contents"
    date_class_tag = "cnn-search__result-publish-date"

    search_results = soup.find_all("div", {"class": search_result_class_tag})

    recent_result = search_results[0]
    oldest_result = search_results[len(search_results) - 1]

    first_soup = recent_result.find("div", {"class": date_class_tag}).find("span", {"class": None})
    last_soup = oldest_result.find("div", {"class": date_class_tag}).find("span", {"class": None})

    earliest_object = get_datetime_object(first_soup)
    latest_object = get_datetime_object(last_soup)
    return (earliest_object, latest_object)

def get_num_results(soup):
    # Looking for the section that looks like:
    # <div class="cnn-search__results-count">
    #  Displaying results 1-1 out of 831 for
    #  <strong>     REMOVE
    #   Elon Musk   REMOVE
    #  </strong>    REMOVE
    # </div>

    num_results_class_tag = "cnn-search__results-count"
    search_results = soup.find("div", {"class": num_results_class_tag})

    # Removing all children that stop us from finding the string
    # https://stackoverflow.com/questions/40660273/in-beautifulsoup-ignore-children-elements-while-getting-parent-element-data
    for child in search_results.find_all():
        child.decompose()

    num_results_string = search_results.string
    num_results_string = num_results_string.split("out of ")[1]
    num_results_string = num_results_string.replace(" for", "")
    return int(num_results_string)

def get_datetime_object(soup):
    date_string = soup.string.strip().replace(",", "")
    return datetime.datetime.strptime(date_string, '%b %d %Y')

def make_date_string(datetime_object):
    return str('%02d' % datetime_object.month) + "/" + str('%02d' % datetime_object.day) + "/" + str(datetime_object.year)