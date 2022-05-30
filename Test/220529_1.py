import math

n = int(input())

numbers = [int(input()) for _ in range(n)]
check = 0

# 완전 제곱수 판별 : 제곱근의 정수형을 다시 제곱해서 원래 수가 나오면 완전 제곱수
for number in numbers:
    if int(math.sqrt(number)) ** 2 == number:
        check += 1

print(check)