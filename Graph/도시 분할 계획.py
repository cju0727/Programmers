# 최소 신장트리를 만들고 거기서 가장 큰 간선을 제거하면 최소 신장트리를 2개 만드는 것과 같다.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # 모든 길의 유지비의 합
        result += cost
        # 최소 신장트리를 2개로 나누기 위해 없애는 길의 값
        last = cost

print(result - last)