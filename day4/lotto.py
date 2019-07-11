import random
import pprint # 화면 정렬해서 보이게 해줌
import requests
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=864"
# 1. 요청
# json
# 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
# 응답 (HTML, XML, JSON)
response = requests.get(url).json() # .html은 .text()
# print(response.json())
# print(response)
# pprint.pprint(response)
# print(type(response))

# 내가 뽑은 로또 번호
my_lotto = random.sample(range(1, 46), 6)

# 몇개 맞았는지
match_count = 0

# 뽑힌 로또 번호
lotto_list = []

# 등수 몇 번 했는지
rank_list = [0, 0, 0, 0, 0, 0]

for i in range(10000000):
    # 당첨번호 6개, 보너스번호는 bonus = response['bonusNo']
    for i in range(6): # for i in range(1, 7):
        lotto_list.append(response['drwtNo'+str(i+1)])
    bonus = response['bnusNo']
    # print(lotto_list)

    # 몇 개 맞았는지 확인
    # for num in my_lotto:
    #     if num in lotto_list:
    #         match_count += 1
    
    # 몇 개 맞았는지 확인
    match_count = len(set(lotto_list) & set(my_lotto)) # & : 교집합, set() : 집합으로 변환, len() : 맞춘 개수

    if match_count == 6:
        # print('1등')
        rank_list[0] += 1
    elif match_count == 5 and bonus in my_lotto:
        # print('2등')
        rank_list[1] += 1
    elif match_count == 5:
        # print('3등')
        rank_list[2] += 1
    elif match_count == 4:
        # print('4등')
        rank_list[3] += 1
    elif match_count == 3:
        # print('5등')
        rank_list[4] += 1
    else:
        # print('다음 기회에...')
        rank_list[5] += 1
    print(rank_list, end='\r')
    my_lotto = random.sample(range(1, 46), 6)
    match_count = 0
    lotto_list = []
print('끝')
print(rank_list)

# rank = 0
# for i in rank_list:
#     print(f'{rank + 1}등 : {i}번')
#     rank+=1

# test=range(1,3)
