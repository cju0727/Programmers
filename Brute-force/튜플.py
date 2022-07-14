def solution(s):
    answer = []
    
    # 아래 작업을 위한 사전 정의 요소들
    string = s[1:-1]
    tmp = ''
    tmp_list = []
    s_list = []
    
    # 중괄호로 감싸져 있는 수들을 리스트 형태로 만드는 작업
    for s in string:
        if s == '}':
            tmp_list.append(tmp)
            s_list.append(tmp_list)
            tmp = ''
            tmp_list = []
        else:
            if s.isdigit():
                tmp += s
            elif s == ',' and tmp != '':
                    tmp_list.append(tmp)
                    tmp = ''
                    
    # s_list의 각 원소의 수가 적은 순서대로 정렬
    s_list.sort(key=lambda x:len(x))
    
    # s_list의 각 리스트의 모든 원소를 answer에 중복되지 않게 넣어준다.
    for s_unit in s_list:
        for s in s_unit:
            if int(s) not in answer:
                answer.append(int(s))
                
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))