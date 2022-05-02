# 같은 팀 여부 확인
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 팀 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 학생 번호와 연산 갯수 입력
n, m = map(int, input().split())
# 학생들의 팀 적는 변수를 정의하고 각 번호로 초기화
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

# 연산 갯수만큼 반복해서 연산을 입력받아줌
for i in range(m):
    bin, a, b = map(int, input().split())
    # 만약 bin이 0이라면 팀 합치기 수행
    if bin == 0:
        union_parent(parent, a, b)
    # 그렇지 않다면 같은 팀 여부 확인 수행
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")