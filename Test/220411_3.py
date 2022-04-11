def solution(A):
    result = 0
    temp = 0

    for i in range(len(A)):
        if A[temp] > A[i]:
            temp = i

        if i != 0 and A[i-1] < A[i] and A[temp] < A[i-1]:
            result += 1
            temp = i-1
    
    if A[temp] < A[i]:
        result += 2
    else:
        result += 1
    
    return result