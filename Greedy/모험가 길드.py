n = int(input())

fears = list(map(int, input().split()))
fears.sort(reverse = True)
count = 0
temp = []

for fear in fears:
    temp.append(fear)
    if len(temp) == max(temp):
        count += 1
        temp = []

print(count)    