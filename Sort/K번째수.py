def solution(array, commands):
    answer = []
    # commands의 갯수만큼 반복
    for i in range(len(commands)):
        # 각 commands의 0번째부터 1번째 인덱스의 숫자를 이용해 array를 슬라이싱
        cut_arr = sorted(array[commands[i][0]-1:commands[i][1]])
        # 각 commands의 2번째 인덱스의 숫자를 이용해 cut_arr의 수를 answer에 삽입
        answer.append(cut_arr[commands[i][2]-1])
    return answer