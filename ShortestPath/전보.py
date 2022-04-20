import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, start = map(int, input().split()) # 노드의 갯수, 간선의 갯수, 시작 위치

graph = [[] for i in range(n + 1)] # 노드의 정보 담는 리스트

distance = [INF] * (n + 1)

# 간선 정보 입력 받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 출력을 위해 변수 사전생성
count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외하고 출력
print(count - 1, max_distance)
