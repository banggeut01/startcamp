# window - cp949 (encoding)
# mac/web... - utf-8
with open ('ssafy_with.txt', 'r') as f:
    # print(f.read())
    # print(f.readlines())
    # 리스트로 읽기
    lines = f.readlines()

print(lines)
for line in lines:
        print(f'print(line) : {line}')
        # strip() : 양쪽 공백 없애줌
        # print(f'print(line.strip()) : {line.strip()}\n')

with open('ssafy.txt', 'r') as f:
    # read : 전체 내용을 하나의 string으로 반환한다.
    txt = f.read()

print(txt)
print(type(txt))