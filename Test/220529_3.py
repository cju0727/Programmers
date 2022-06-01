# n이 클 때, 시간 초과되는 풀이
n = int(input())

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

is_prime = True
prime = []

for i in range(10 ** (n-1), 10 ** n):
    if n != 1:
        if is_prime_number(i):
            is_prime = True
            for j in range(1, n):
                k = int(str(i)[:n-j])
                if not is_prime_number(k):
                    is_prime = False
                    break
            
            if is_prime:
                prime.append(str(i))
    else:
        if is_prime_number(i):
            prime.append(str(i))

print(" ".join(prime))