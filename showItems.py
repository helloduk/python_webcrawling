import urllib.request
from bs4 import BeautifulSoup

data = urllib.request.urlopen('https://finance.naver.com/item/main.nhn?code=032620')

soup = BeautifulSoup(data, 'html.parser')

# <div class="rate_info"><div class="today">
#     <p class="no_today">
#         <em class="no_up">
#             <span class="no1">1</span>
#             <span class="no2">2</span>
#             <span class="shim">,</span>
#             <span class="no1">1</span>
#             <span class="no5">5</span>
#             <span class="no0">0</span>
#         </em>
#     </p>

list = soup.find_all('div', attrs={'class':'rate_info'})

for item in list:
    try:
        title = item.find('p').get_text()
        print(title.strip())
    except:
        pass