n, m = map(int, input().split())

ball = list(map(int, input().split()))

# 시간이 오래걸리는 풀이
# count = 0

# for i in range(n):
#     for j in range(i + 1, n):
#         if ball[i] != ball[j]:
#             count += 1

# print(count)

# 효율적인 풀이
count = 0

array = [0] * 10
for b in ball:
    array[b] += 1

for i in range(1, m + 1):
    n -= array[i]
    count += array[i] * n

print(count)