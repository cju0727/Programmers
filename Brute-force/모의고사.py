def solution(answers):
    answer = []
    count = [0, 0, 0]
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, a in enumerate(answers):
        if a == pattern1[i%len(pattern1)]:
            count[0] += 1
        if a == pattern2[i%len(pattern2)]:
            count[1] += 1
        if a == pattern3[i%len(pattern3)]:
            count[2] += 1

    for idx, c in enumerate(count):
        if c == max(count):
            answer.append(idx + 1)
    return answer