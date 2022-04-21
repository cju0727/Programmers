# 각 원소가 속한 집합을 나타내는 함수
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 각 원소의 연결을 확인해 부모 노드를 바꾸는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수(v)와 간선의 개수(e)
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 각 노드의 부모를 각자의 번호로 설정
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end = '')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')

print()

print('부모 테이블: ', end = '')
for i in range(1, v + 1):
    print(parent[i], end = ' ')