def check_good_string(string):
    check = []
    for s in string:
        if check and check[-1] == "(" and s == ")":
            check.pop()
        else:
            check.append(s)
    if check:
        return False
    else:
        return True

def check_bal_string(string):
    check = 0
    for s in string:
        if s == "(":
            check += 1
        else:
            check -= 1
    if check != 0:
        return False
    else:
        return True
    
def change_string(string):
    # 1
    if not string:
        return string
    else:
        # 2
        for i in range(len(string)):
            if check_bal_string(string[:i+1]):
                u = string[:i+1]
                v = string[i+1:]
                # 3
                if check_good_string(u):
                    v = change_string(v)
                    return u + v
                # 4
                else:
                    # 4-1, 2, 3
                    v = change_string(v)
                    new = "(" + v + ")"
                    # 4-4
                    u = u[1:-1]
                    for i in u:
                        if i == "(":
                            new += ")"
                        else:
                            new += "("
                            
                    return new  

def solution(p):
    answer = change_string(p)
    return answer

p = "(()())()"
print(solution(p))