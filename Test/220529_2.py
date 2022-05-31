start, end = map(int, input().split())

result = 0

for i in range(start, end + 1):
    result += int(str(i)[0]) * int(str(i)[1])

print(result)