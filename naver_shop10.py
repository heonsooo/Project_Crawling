import requests 
from bs4 import BeautifulSoup

url = 'https://search.shopping.naver.com/best100v2/main.nhn'

# request로 특정 사이트 html 긁어오기
request = requests.get(url)

# bs4로 html 파싱 
html = request.text
soup = BeautifulSoup(html, 'html.parser')

# 내가 원하는 태그(<a class="link_text"> 찾아서 
links = soup.find_all('a', '_popular_srch_lst_li')

# 쇼핑 상위 10 선정 기준 날짜 
date = soup.select_one('#realtimeRankArea > div.popular_area > h3 > em')


# for문으로 하나씩 꺼냄
result = []
for link in links:    
    link = link.text
    result.append(link.replace(' ',''))

print(date.text)
print(result)