# 떡의 갯수 n과 요청한 떡의 길이 m
# 떡의 높이가 주어지고 이때 설정할 수 있는 절단기의 최댓값을 구하는 문제

n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for a in array:
        if a > mid:
            total += a - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)