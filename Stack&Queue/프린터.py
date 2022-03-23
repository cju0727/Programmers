def solution(priorities, location):
    answer = 0
    count = 0
    stack = []
    
    # 처음 priorities의 index와 value를 stack에 담아준다.
    for i, n in enumerate(priorities):
        stack.append((i, n))
    
    # while문을 이용해 매 stack의 첫번째를 가지고 판단해 조작한다.
    while True:
        # stack의 첫 value가 가장 높은 중요도가 아닌 경우 stack의 맨 뒤로 보내준다.
        if stack[0][1] != max(priorities):
            stack.append(stack.pop(0))
        # stack의 첫 value가 가장 높은 중요도인 경우 stack에서 빼고 count를 센다
        else:
            count += 1
            priorities.remove(max(priorities))
            check = stack.pop(0)
            # check에 빼준 값을 넣어두고 만약 그 index가 location과 같을 경우 쌓인 count를 return 해준다.
            if check[0] == location:
                answer = count
                break
                
    return answer