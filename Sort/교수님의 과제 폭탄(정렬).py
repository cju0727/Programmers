n = int(input())
result = "Yes"

calendar = []
for i in range(n):
	start, end = input().split()
	start_month, start_day = map(int, start.split('/'))
	end_month, end_day = map(int, end.split('/'))
	calendar.append((start_month, start_day, end_month, end_day))

calendar.sort(key = lambda x : (x[0], x[1] -x[2], -x[3]))

for i in range(n - 1):
	if calendar[i][2] < calendar[i + 1][2] or (calendar[i][2] == calendar[i + 1][2] and calendar[i][3] < calendar[i + 1][3]):
		result = "No"
		print(result)
		break
		
if result == "Yes":
	print(result)