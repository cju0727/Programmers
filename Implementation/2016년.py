def solution(a, b):
    answer = ''
    count = 0
    day_name = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    day_num = [30, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 1월이 아닐 경우 주어진 1월과 a월 사이의 일수를 더하고 b를 더해서 카운트한다.
    if a != 1:
        for m in range(0, a - 1):
            count += day_num[m]
        count += b
    # 1월인 경우 b에서 1만큼 뺀 수를 카운트한다.
    else:
        count += (b - 1)

    # 움직인 위치에 있는 요일을 리턴한다.
    start_idx = 0
    idx = (start_idx + count) % 7
    answer = day_name[idx]
    return answer


a = 5
b = 24
print(solution(a, b))
