def solution(record):
    answer = []
    uid = {}
    
    for r in record:
        r = r.split()
        if len(r) == 3:
            uid[r[1]] = r[2]
    
    for r in record:
        r = r.split()
        if r[0] == "Enter":
            answer.append("%s님이 들어왔습니다." %uid[r[1]])
        elif r[0] == "Leave":
            answer.append("%s님이 나갔습니다." %uid[r[1]])
            
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
"Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))