def solution(n, lost, reserve):
    
    # 체육 수업 참가 학생 수 = 전체 학생 수 - 체육복 잃어버린 학생 수
    answer = n - len(lost)

    # 체육복 잃어버린 학생 수 만큼 반복
    for i in lost:
        
        # 자신의 양 옆의 학생에게 체육복을 빌릴 수 있으면 빌리고 체육 수업 참가
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
        
    return answer