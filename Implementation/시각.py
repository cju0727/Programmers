n = int(input())

count = 0

# 0시 ~ n시까지
for i in range(n + 1):
    # 0분 ~ 59분까지
    for j in range(60):
        # 0초 ~ 59초까지
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)