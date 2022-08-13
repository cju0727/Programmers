def solution(arr):
    answer = []
    for a in arr:
        # 첫번째 인덱스의 값 처리
        if not answer:
            answer.append(a)
        # 연속적으로 나타나는 숫자가 바뀔 경우 값을 answer에 넣어준다.
        if answer[-1] != a:
            answer.append(a)
    return answer


arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))
