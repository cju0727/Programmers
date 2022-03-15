def solution(participant, completion):
    # 해시 값을 담을 딕셔너리 생성
    hashDict = {}
    sumHash = 0
    
    # participant 원소들의 해시값을 다 더해줌
    for p in participant:
        hashDict[hash(p)] =  p
        sumHash += hash(p)
        
    # sumHash 에서 completion 원소들의 해시값을 빼면 완주하지 못한 선수의 hash만 남게된다.
    for c in completion:
        sumHash -= hash(c)
        
    return hashDict[sumHash]