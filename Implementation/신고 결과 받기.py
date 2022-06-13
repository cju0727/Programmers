from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    lst = defaultdict(set)
    check = defaultdict(int)
    black_lst = []

    for r in report:
        user, bully = r.split()

        check[bully] += 1
        lst[user].add(bully)

        if check[bully] == k:
            black_lst.append(bully)

    for b in black_lst:
        for i in range(len(id_list)):
            if b in lst[id_list[i]]:
                answer[i] += 1
    
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))