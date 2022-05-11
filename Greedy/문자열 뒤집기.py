# 0과 1로 이루어진 문자열 S가 주어진다.
# 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 연속된 숫자 하나 이상을 잡고 뒤집는다.
# 뒤집는 행동 한번을 1회라고 했을 때 모든 숫자를 같게 만드는 최소 횟수를 구하라.

S = input()

# 0그룹, 1그룹, 그룹을 나누는 기점이 되는 수를 체크한다.
zero = 0
one = 0
first = 0

for i, s in enumerate(S):
    # i가 0일때의 문자를 첫 기점으로 삼는다.
    if i == 0:
        first = s
        continue
    # 기점과 다른 문자가 나왔을 때, 그 이전 그룹이 0인 경우 zero에 1을 더한다.
    if s != first and first == '0':
        zero += 1
        first = s
    # 기점과 다른 문자가 나왔을 때, 그 이전 그룹이 1인 경우 one에 1을 더한다.
    elif s != first and first == '1':
        one += 1
        first = s
# 마지막 그룹은 문자가 바뀌지 않으므로 위의 방시에서 체크가 안된다,
# 따라서 따로 체크해준다.
if first == '0':
    zero += 1
else:
    one += 1

# 각 그룹의 갯수를 체크했다면 더 적은 갯수의 그룹을 출력한다.
print(min(zero, one))