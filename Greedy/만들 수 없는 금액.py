# N개의 동전이 있을 때 이를 이용해 만들 수 없는 가장 작은 양의 정수 금액
    # N = 5, 3 2 1 1 9원짜리 동전이 있다고 가정.
    # 8원을 만들 수 없음.

N = int(input())

cost = list(map(int, input().split()))
cost.sort()

target = 1
for c in cost:
    if target < c:
        break
    target += c

print(target)
