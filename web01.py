import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('https://helloduk.github.io/')

soup = BeautifulSoup(page, 'html.parser')

print(soup.find_all("div"))