# import required modules
import wikipedia
from bs4 import BeautifulSoup
import requests

print(wikipedia.page("Android (robot)").content)
# get URL
# page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
# # scrape webpage
# soup = BeautifulSoup(page.content, 'html.parser')
# list(soup.children)
# # find all occurance of p in HTML
# # includes HTML tags
# print(soup.find_all('p'))
# print('\n\n')
# # return only text
# # does not include HTML tags
# print(soup.find_all('p')[0].get_text())
