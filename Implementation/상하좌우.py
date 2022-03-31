n = int(input())
commands = list(map(str, input().split()))

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

types = ['U', 'D', 'L', 'R']

for c in commands:
    for i in range(len(types)):
        if c == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or  ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(y, x)