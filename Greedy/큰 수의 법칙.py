n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse = True)
first = data[0]
second = data[1]


# 가장 큰 수가 더해지는 횟수를 구한다.
count = m // (k+1) * k
count += m % (k+1)

result = 0
result = count * first
result += (m - count) * second

print(result5 8)