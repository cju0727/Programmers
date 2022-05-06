from collections import deque
import copy

v = int(input())

indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]
time = [0] * (v + 1)

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    # 리스트의 경우 단순 대입 시 값이 변할 우려가 있으므로 복사를 해준다.
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, v + 1):
        print(result[i])

topology_sort()