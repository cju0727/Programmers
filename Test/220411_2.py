def solution(A, B):
    if set(A) != set(B):
        return False
    temp = B

    while A != B:
        B.append(B.pop(0))
        if A == B:
            return True
        if B == temp:
            return False