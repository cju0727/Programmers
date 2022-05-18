from curses.ascii import isalpha


S = input()

# 알파벳으로 이루어진 문자를 담을 리스트
string = []
# 숫자를 담을 리스트
number = []

# 입력값을 한글자씩 돌면서
for s in S:
    # 알파벳일 경우 string으로
    if s.isalpha():
        string.append(s)
    # 숫자일 경우 number로
    else:
        number.append(int(s))

# string 리스트는 정렬해주고
string.sort()

# string 뒤에 숫자의 합을 더해서 출력해준다.
print(''.join(string) + str(sum(number)))
