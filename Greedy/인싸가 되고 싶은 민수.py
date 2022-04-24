# 1. 두 정수가 주어졌을 때, 그 수를 포함한 사이에 존재하는 수를 파악할 것.
# 2. 각 수들의 약수의 갯수를 체크하고 가장 많은 수를 출력할 것. (1은 제외)
# 3. 정답이 여러 개일 경우 가장 작은 수를 출력하도록 할 것.

a, b = map(int, input().split())

# 시간초과가 발생하는 풀이
# check = [0] * (b - 1) # 10개의 원소를 가지고 있는 리스트 (0번째 값은 2의 값이다.)

# for i in range(a, b + 1): # 1부터 10까지
# 	if i == 1:
# 		continue
# 	else:
# 		for j in range(2, i + 1): 
# 			if i % j == 0:
# 				check[j - 2] += 1

# print(check.index(max(check)) + 2)

# 옳은 풀이 
result = 0

# 2 이상의 수에서는 가장 많은 수의 약수를 가지는 수는 2이다.
if a != b: 
	print(2)
else: # a == b인 경우에는 약수의 개수를 비교하는 것이 무의미. 작은 값 찾는다.
	for i in range(2, int(a ** 0.5) + 1):
		# a가 소수가 아닌 경우 a의 약수 중 가장 작은 값을 출력
		if a % i == 0:
			result = i
			print(i)
			break
  # a가 소수일 경우 자기 자신을 출력
	if result == 0:
		print(a)