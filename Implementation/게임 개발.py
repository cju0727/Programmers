n, m = map(int, input().split())

x, y, d = map(int, input().split())

real_fields = []
for i in range(n):
    real_fields.append(list(map(int, input().split())))

check_fields = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

check_fields[x][y] = 1
result = 1
turn_count = 0

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if check_fields[nx][ny] == 0 and real_fields[nx][ny] == 0:
        check_fields[nx][ny] = 1
        x = nx
        y = ny
        result += 1
        turn_count = 0
        continue

    else:
        turn_count += 1
    
    if turn_count == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if real_fields[nx][ny] == 0:
            x = nx
            y = ny
            turn_count = 0
        else:
            break

print(result)