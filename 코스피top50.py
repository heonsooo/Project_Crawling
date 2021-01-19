import csv
import requests
import lxml
from bs4 import BeautifulSoup

filename = '시가총액(Top50).csv'
f = open(filename,'a',encoding='utf-8-sig',newline='')

import csv
writer = csv.writer(f)
title = [i for i in range(0,51)]
# writer.writerow(title)

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?&page='
page = 1
res=requests.get(url+str(page))
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

import datetime
today = datetime.datetime.now().strftime('%Y-%m-%d')
co = [today]
for row in data_rows:
    columns = row.find_all('td')
    if len(columns) <= 1:
        continue
    data = [column.get_text().strip() for column in columns]
    co.append(data[1])
    # print(data)
    # writer.writerow(data)

# print(len(co))
writer.writerow(co)