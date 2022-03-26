def solution(rounds):
    couple = []
    excouple = []

    rule = []
    answer = 0
    dict = {}
    abcd = ["a", "b", "c", "d"]
    for round in rounds:
        for i, alpha in enumerate(abcd):
            dict[alpha] = round[i]

        for j, alpha in enumerate(abcd):
            if alpha == dict[dict[alpha]] and alpha != dict[alpha]:
                couple.append(alpha)

            if alpha == dict[alpha] or (dict[alpha] in excouple and alpha in excouple):
                rule.append(alpha)

        answer += len(rule)
        rule = []
        excouple = []
        excouple.extend(couple)
        couple = []

    return answer