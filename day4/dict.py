# dictionary
# key - value
# key : string, integer, float, boolean 
# / list, dictionary는 key가 될 수 없다.
# value : 모든 값을 가질 수 있다.

# lunch = {'중국집' : '044-885-9874'}
# print(lunch)
# dinner = dict(한식='042-888-9999')
# print(dinner)
# bf = {}
# bf['분식'] =  '012-5554-5455'
# print(bf)

# menu = {'bf' : bf, 'lunch' : lunch, 'dinner' : dinner}
# print(menu)
# # 중첩된 형식의 dictionary 접근
# print(menu['bf']['분식'])

ssafy = {'김은정' : '학생', '김인성' : '학생', '연용흠' : '반장'}
for key in ssafy:
    print(key)
    # key값 출력
    print(ssafy[key])
    # value값 출력

# key, value 같이 출력
for key, value in ssafy.items():
    print(key, value)
# print(ssafy.items())
# 튜플들이 여러개 모여있는 리스트 형태 / key와 value를 가지는 튜플들

# value값만 출력
for value in ssafy.values():
    print(value)

# key값만 출력
for key in ssafy.keys():
    print(key)