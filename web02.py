from bs4 import BeautifulSoup

page = open('d:\\GitHub\\helloduk.github.io\\index.html', 'rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())

#print(soup.find_all('p'))

#<section class='box style1'>
print(soup.find('section', class_='box style1'))
print(soup.find('section', class_='box style1').get_text())

for tag in soup.find_all('section'):
    print(tag.get_text())