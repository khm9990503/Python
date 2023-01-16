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

# HTML 요청
url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20230116&page=1'

html = req.get(url, headers={'User-Agent':'Mozilla/5.0'}).text
#print(html) # 비정상적 접속으로 막음

# 문서 객체 생성
dom = bs(html, 'html.parser')
tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')

print('tit : ',tit)
for li in lis:
    title = li.select_one('dl > dt:not(.photo) > a').text
    content = li.select_one('dl > dd > span.lede').text
    pub = li.select_one('dl > dd > span.writing').text
    time = li.select_one('dl > dd > span.date').text
    print('title : ',title.strip())
    print('content : ',content.strip())
    print('pub : ',pub.strip())
    print('time : ',time.strip())
