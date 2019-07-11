# d4-1.py
"""
Python dictionary 연습 문제
"""

# # 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 - 기본풀이 ====')
result = 0
count = 0

for score_value in score.values():
    result += score_value
    count+=1 
print(result/len(score))

print('==== Q1 - sum 함수 활용하기 ====')
# score.values() => dict_values([80, 90, 100])
# type(score.values()) => <class 'dict_values'>
# b = (1,2,4) sum(b)=> 7 숫자로 이루어진 튜플도 sum 된다. 숫자 요소로 이루어진 리스트, 튜플 등...
result2 = sum(score.values())
count = len(score)
print(result2/count)



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 - 반 평균 ==== (내 풀이)')
result = 0
for class_name in scores.keys():
    # print(scores[class_name].values())    
    for score in scores[class_name].values():
        result = result + score
    print(f'{class_name} : {result/len(scores[class_name])}')
    result = 0

print('==== Q2 - 전체 평균 ====')
total_score = 0
count = 0
for person_scores in scores.values():
    # print(person_scores)
    for score in person_scores.values():
        total_score += score
        count += 1
print(total_score/count)



# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 (내 풀이) ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# result = 0
for area in city.keys():
    result = sum(city[area])
    # for tem in city[area]:
    #     result = result + tem
    print(f'{area} : {result/len(city[area])}')
    # result = 0

print('==== Q3-1 ====')
for name, temp in city.items():
    avg = sum(temp)/len(temp)
    print(f'{name} : {avg:.2f}') # f-string : 3.6+:.2f소수점 두 번째자리까지
    print('{} {:.2f}'.format(name, avg)) #format-string
    print(name + ' : ' + str(avg)) #????????avg 왜 str 씌워야하는지?

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 (내 풀이) ====')
for i in range(3):
# 3일 동안
    day_tem = []
    for area in city.keys():
        day_tem.append(city[area][i])
    max_tem = max(day_tem)
    min_tem = min(day_tem)
    for area in city.keys():
        if max_tem == city[area][i]:
            print(f'{i+1}일 가장 더웠던 지역은 {area}입니다.')
        if min_tem == city[area][i]:
            print(f'{i+1}일 가장 추웠던 지역은 {area}입니다.')

print('==== Q3-2 ====')
min_temp = 0
max_temp = 0
min_city = ''
max_city = ''
count = 0
# 모든 지역의 온도를 모두 확인하면서,
for name, temp in city.items(): # print (name, temp) => 서울 [-6, -10, 5] ...
    # 첫 번째 반복 때는 모두 다 저장해!
    if count == 0:
        min_city = name
        max_city = name
        min_temp = min(temp)
        max_temp = max(temp)
        count += 1
# 가장 추우면, 해당 도시와 기온을 기록
    if min(temp) < min_temp:
        min_city = name
        min_temp = min(temp)
# 더울 때도, 해당 도시와 기온을 기록
    if max(temp) > max_temp:
        max_city = name
        max_temp = max(temp)
print(f'추운 곳은 {min_city}, 더운 곳은 {max_city}')

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 내 풀이====')
# boolean = False
# for tem in city['서울']:
#     if tem == 2:
#         boolean = True
# print(boolean)

# 리스트 검사 
# >>> 0 in range(5) # => True
if 2 in city['서울']: # 'a' in 'apple' => True
    print('네!')
else:
    print('아니오!')

>>> 0 in range(5)
