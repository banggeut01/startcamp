# number.txt를 읽어서
with open('number.txt', 'r') as file:
    numbers = file.readlines()
print(numbers)

# 리스트를 뒤집는다.
numbers.reverse()

# number_reverse.txt로 저장!
with open('number_reverse.txt', 'w') as file:
    for number in numbers:
        file.write(number)