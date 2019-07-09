import os

# 1. dummy 폴더로 이동한다.
os.chdir('./dummy')
print(os.getcwd())

# 2. 하나하나씩 파일명을 변경한다. -> 반복문
files = os.listdir('.')
print(files)
print(type(files))
for file in files:
# for file in os.listdir:
    os.rename(file, file.replace('SAMSUNG', 'SSAFY'))
    # os.rename(file, 'SAMSUNG'+file)
print(os.listdir('.'))

