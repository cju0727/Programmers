def solution(sizes):
    answer = 0
    w = []
    h = []

    for size in sizes:
        w.append(max(size[0], size[1]))
        h.append(min(size[0], size[1]))

    answer = max(w) * max(h)

    return answer


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
