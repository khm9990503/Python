"""
날짜 : 2023/01/17
이름 : 구홍모
내용 : 파이썬 가상브라우저 실습하기


반응형 웹을 크롤링 하기
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 가상브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# naver 이동
browser.get('https://naver.com')

# login 클릭
btnLogin = browser.find_element(By.CSS_SELECTOR,'#account > a')
btnLogin.click()

# 아이디 비번 입력
input_id = browser.find_element(By.CSS_SELECTOR,'#id')
input_pw = browser.find_element(By.CSS_SELECTOR,'#pw')
input_id.send_keys('asdf')
input_pw.send_keys('1234')

# 최종 로그인 클릭
btnSub = browser.find_element(By.CSS_SELECTOR,'#log\.login')
btnSub.click()
