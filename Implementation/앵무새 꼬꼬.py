n = int(input())
target = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ''

for i in range(n):
	sentence = input()
	
	for s in sentence:
		if s in target:
			result += s
	if result == '':
		print("???")
	else:	
		print(result)
		result = ''