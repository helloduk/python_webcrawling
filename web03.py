from bs4 import BeautifulSoup
import re

doc = ['<html><head><title>Page title</title></head>',\
    '<body><p id="firstpara" align="center">This is paragraph <b>one</b></p>',\
    '<p id="secondpara" align="blah"> This is a paragraph <b>two</b></p>', '</html>']

soup = BeautifulSoup(''.join(doc),'html.parser')
#태그를 정렬해서 보여주기
#print(soup.prettify())

#b로 시작하는 tag들 보여주기
# tagsStartingWighB = soup.findAll(re.compile('^b'))
# print([tag.name for tag in tagsStartingWighB])

#print(soup.find_all(['title','p']))

#lamda 함수 정의
#print(soup.find_all(lambda tag:len(tag.attrs)==2))

#para로 끝나는 tag들 보여주기
# print(soup.find_all(id=re.compile('para$')))

soup = BeautifulSoup("""
    Bob's<b>Bold</b>Barbeque Sauce now available
    <b class="hickory">Hickory</b>and <b class="lime">Lime</a>
    """, "html.parser")

#<b class='lime'>content</b> 찾기
#BeautifulSoup만으로는 아래와 같은 형태로 찾을 수 있지만, re(Regular Expression)을 통하면 보다 강력하게 검색가능
print(soup.find('b', {'class':'lime'}))
print(soup.find('b', {'class':'lime'}).get_text())