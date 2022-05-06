# 위상 정렬 알고리즘에 사용할 deque
from collections import deque
# 리스트 값 복사를 위한 copy
import copy

v = int(input())

#모든 노드의 진입 차수를 0으로 초기화
indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    # 걸리는 시간
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