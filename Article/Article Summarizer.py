import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'http://python.org'
response = urlopen(url)
html = response.read()

#print html
# We can use BeautifulSoup to parse the web tree to give us only the web-links instead.
soup = BeautifulSoup(html, "html.parser")

apiKey = 64C5D2EFE9
text = ""
url = "http://api.smmry.com/&SM_API_KEY={}&sm_api_input={}".format(apiKey, text)

response = urlopen(url)

print(response.read().decode('utf-8'))