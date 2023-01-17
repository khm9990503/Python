"""
날짜 : 2023/01/16
이름 : 구홍모
내용 : 파이썬 HTML 파싱 실습하기

파싱 : 구문분석, 추출

"""

import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
import time

# 엑셀파일 생성
Workbook = Workbook()
sheet = Workbook.active

pg = 1
count = 0

while True:
    # HTML 요청
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20230117&page=%d' % pg

    html = req.get(url, headers={'User-Agent':'Mozilla/5.0'}).text
    #print(html) # 비정상적 접속으로 막음

   

    # 문서 객체 생성
    dom = bs(html, 'html.parser')
    tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
    lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')
    current = dom.select_one('#main_content > div.paging > strong').text

    if pg > int(current):
        break

    # print('tit : ',tit)
    for li in lis:
        tag_a = li.select_one('dl > dt:not(.photo) > a')
        title = tag_a.text
        link = tag_a['href']
        content = li.select_one('dl > dd > span.lede').text
        pub = li.select_one('dl > dd > span.writing').text
        time = li.select_one('dl > dd > span.date').text

       # print('count : ',count)
       # print('title : ',title.strip())
       # print('link : ',link.strip())
       # print('content : ',content.strip())
       # print('pub : ',pub.strip())
       # print('time : ',time.strip())
        count += 1
        sheet.append([count,title.strip(),link.strip()])
        print('%d건 저장' % count)

        
    pg += 1
# excel save
Workbook.save('C:/Users/java1/Desktop/naver.xlsx')
print('종료...')
