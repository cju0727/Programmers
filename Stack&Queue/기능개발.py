import math

def solution(progresses, speeds):
    answer = []
    pro = []
    stack = []
    count = 0
    
    # 모든 반복은 progresses의 갯수만큼 반복
    for i in range(len(progresses)):
        # pro에 각 작업의 작업일수 기입(math.ceil로 소숫점 올림 사용)
        pro.append(math.ceil((100 - progresses[i]) / speeds[i]))
        # stack에 아무 숫자도 없을 시 바로 채워줌
        if not stack:
            stack.append(pro[i])
            count += 1
        # stack에 이미 크거나 같은 수가 들어있을 경우 count만 채워준다.
        elif stack[-1] >= pro[i]:
            count += 1
        # stack에 들어있는 수보다 들어갈 수가 더 클 경우 count를 answer에 넣어주고 스택을 바꿔준다.
        else:
            stack.pop()
            answer.append(count)
            count = 0
            stack.append(pro[i])
            count += 1
    
    answer.append(count)

    return answer