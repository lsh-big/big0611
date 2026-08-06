import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# 동적 웹 크롤링
# selenium(v4.46.0)으로 실습하기
# 구글 크롬 브라우저: chrome://version/
# 버전 151.0.7922.76(공식 빌드) (64비트)
# https://sites.google.com/a/chromium.org/chromedriver/downloads -> 접속x
# https://googlechromelabs.github.io/chrome-for-testing/
# c:\LSH\big0611\py\p03_크롤링\ch02_selenium
# c:\LSH\big0611\py\p03_크롤링\ch02_selenium\chromedriver.exe

# 셀레니움 3.x 이전
# 드라이버에 속한 경로에 한글명이 없어야 한다.
# driver = webdriver.Chrome('E:\\wi\\git\\big0611\\py\\p03_크롤링\\ch02_selenium\\chromedriver.exe')
# driver = webdriver.Chrome('E:/wi/dev0611/chromedriver-win64/chromedriver.exe')

# 셀레니움 4.x 이후
# 1. 회사에서 인터넷이 차단되어 있어 Selenium Manager가 드라이버를 다운로드할 수 없는 경우
# 2. Chrome(Stable, Beta, Dev)이 여러 개 설치되어 그 브라우저에 맞는 드라이버를 Service로 지정하는 경우
# service = Service('c:\\LSH\\big0611\\py\\p03_크롤링\\ch02_selenium\\chromedriver.exe')

driver = webdriver.Chrome()

driver.implicitly_wait(3)
driver.get('https://www.livesport.com/team/manchester-united/ppjDR086')

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify())

# 승패 기록 페이지 크롤링하고 분석하기

win = soup.find_all('span', class_='wld wld --w')
tie = soup.find_all('span', class_='wld wld --d')
lose = soup.find_all('span', class_='wld wld --l')

print(f"승: {len(win)}")
print(f"무: {len(tie)}")
print(f"패: {len(lose)}")

time.sleep(2) # 2초 대기
driver.quit() # 브라우저 창 닫기 -> 지금은 자동 종료