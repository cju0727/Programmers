# 현재 캐릭터의 점수 N (항상 짝수)
# 자릿수를 기준으로 N을 반으로 나누어 왼쪽과 오른쪽 각각의 자릿수를 더함
# 두 수가 같을 경우 LUCKY, 아닐 꼉우 READY를 출렦

N = input()

# len(N)을 이용해 left와 right를 나눈다.
left = N[:len(N)//2]
right = N[len(N)//2:]

# 왼쪽과 오른쪽의 자릿수를 각각 더해서 비교한다.
sum_left = 0
for l in left:
    sum_left += int(l)

sum_right = 0
for r in right:
    sum_right += int(r)

# 왼쪽과 오른쪽의 합이 서로 같을 경우 LUCKY를 출력한다.
if sum_left == sum_right:
    print("LUCKY")
# 그렇지 않을 경우 READY를 출력한다.
else:
    print("READY")
