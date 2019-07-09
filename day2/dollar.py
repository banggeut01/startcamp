import requests
from bs4 import BeautifulSoup

# # 1. url 설정
# url = 'https://search.naver.com/search.naver?query=환율'
# # 2. 요청 보내기
# response = requests.get(url).text
# # 3. HTML 문서로 바꾸기
# soup = BeautifulSoup(response, 'html.parser')
# # 4. 원하는 내용 선택자로 뽑아내기
# exchange_rate = soup.select_one('#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.dw').text
# print(exchange_rate)

# 1. url 설정
url = 'https://finance.naver.com/marketindex//exchangeList.nhn'
# 2. 요청 보내기
response = requests.get(url).text
# print(response)
# 3. HTML 문서로 바꾸기
soup = BeautifulSoup(response, 'html.parser')
# 4. 원하는 내용 선택자로 뽑아내기
# print(soup)
table = soup.select('body > div > table > tbody > tr')
for tr in table:
    # 아래 두 코드는 같은 결과
    # print(tr.select('td.sale'))
    print(tr.select_one('td.sale').text)
    # select를 쓰면 리스트를 반환함 결과는 원소가 하나인 리스트 반환, 아래와 같이 사용할 수 있음
    # print(tr.select('td.sale')[0].text)    