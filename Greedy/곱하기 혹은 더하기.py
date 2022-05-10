# 숫자로만 이루어진 문자열 S를 입력
S = input()
# 결과값을 담을 result 생성
result = 0
# 문자열의 왼쪽부터 오른쪽으로 순서대로 확인
for i, s in enumerate(S):
    # 가장 왼쪽의 수는 연산이 없으므로 그대로 입력받는다.
    if i == 0:
        result = int(s)
        continue
    # 그 외에는 이전의 수와의 덧셈과 곱셈을 통해 큰 수를 result에 담는다.
    result = max(result + int(s), result * int(s))

print(result)