from itertools import combinations

def solution(places):
    answer = []
    # places를 for문으로 돌면서 개별적으로 거리두기 준수 여부를 판별
    for place in places:
        # 응시자가 앉아있는 자리(P)를 행렬 좌표로 파악 -> p_place
        p_place = []
        for i, p in enumerate(place):
            for j, p in enumerate(p):
                if p == "P":
                    p_place.append((i, j))
        
        # 각 응시자가 앉아있는 자리의 거리두기 여부 판별은 P의 조합으로 판별이 가능
        com = list(combinations(p_place, 2))
        check = True
        for l, r in com:
            # 두 P의 맨해튼 거리가 2 이하일 경우
            if abs(l[0] - r[0]) + abs(l[1] - r[1]) <= 2:
                # 1. 두 P가 같은 행에 있을 때 자리 사이에 X가 없다면 거리두기 X
                if l[0] == r[0]:
                    if place[l[0]][l[1] + 1] != "X":
                        check = False
                        break
                # 2. 두 P가 같은 열에 있을 때 자리 사이에 X가 없다면 거리두기 X
                elif l[1] == r[1]:
                    if place[l[0] + 1][l[1]] != "X":
                        check = False
                        break
                # 3. 두 P가 대각선 위치에 있을 때 자리 사이에 X가 없다면 거리두기 X
                else:
                    if place[l[0]][r[1]] != "X":
                        check = False
                        break
                    elif place[l[0] + 1][l[1]] != "X":
                        check = False
                        break        
        
        # check가 True일 경우 거리두기가 잘 지켜지고 있으므로 1을 담는다.
        if check:
            answer.append(1)
        # check가 False일 경우 거리두기가 잘 지켜지고 있지 않으므로 0을 담는다.
        else:
            answer.append(0)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))