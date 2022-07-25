def change(n, base):
    string = ''

    while n > 0:
        n, r = divmod(n, base)
        string += str(r)

    return string


def solution(n):
    answer = int(change(n, 3), 3)

    return answer


n = 45
print(solution(n))
