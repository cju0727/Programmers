def solution(name):
    cur = 0
    answer = 0
    
    # name 각 자리 문자의 ord수를 이용해 A 또는 Z와 비교해 더 적은 격차를 구해 리스트에 담는다.
    # change는 각 자리별 위아래 최소 이동 횟수를 나타낸다.
    change = [ min(ord(i) - ord('A') , ord('Z') - ord(i) + 1 ) for i in name]

    while True:
        # 커서가 있는 곳의 위아래 최소 이동 횟수를 answer에 담아내고 그 자리를 0으로 바꿔준다.
        answer += change[cur]
        change[cur] = 0
        
        # 커서가 있는 곳을 0으로 바꿔주기 때문에 모든 자리의 합이 0일 경우 solution을 종료한다.
        if sum(change) == 0:
            break
            
        # 좌, 우로 1칸씩 확인해 change가 0일 경우 +1을 해준다.
        left, right = 1, 1
        while change[cur - left] == 0:
            left += 1
            
        while change[cur + right] == 0:
            right += 1
        
        # change가 0이 아닌 위치가 더 가까운 쪽으로 이동하면서 answer와 cur를 바꿔준다.
        answer += left if left < right else right
        cur += -left if left < right else right
        
    return answer