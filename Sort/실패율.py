from collections import Counter

def solution(N, stages):
    answer = []
    num = {}
    # 각 스테이지마다 클리어하지 못한 사용자의 수를 체크
    cnt = Counter(stages)
    
    # 전체 스테이지마다 확인
    for i in range(1, N+1):
        clear = 0
        # 각 스테이지에 도달한 사용자의 수를 체크
        for s in stages:
            if s >= i:
                clear += 1
        # 스테이지의 클리어한 사용자의 수가 0이 아니라면 실패율을 기록
        if clear != 0:
            num[i] = cnt[i] / clear
        # 스테이지의 클리어한 사용자의 수가 0이라면 실패율을 0으로 기록
        else:
            num[i] = 0.0
    
    # {스테이지 : 실패율} 딕셔너리를 value 기준으로 정렬
    nums = sorted(num.items(), key=lambda x: x[1], reverse = True)
    
    # 정렬한 (key, value)에서 key값만 answer에 넣어준다.
    for i in range(N):
        answer.append(nums[i][0])
        
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))