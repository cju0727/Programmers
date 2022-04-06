# 부품 n개, 각 부품은 고유한 정수 번호를 가진다.
# 누군가 m개의 부품을 구매할 때 고유 번호를 이용해 부품이 있으면 yes, 아니면 no

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
buy_list = list(map(int, input().split()))

for i in buy_list:
    result = binary_search(array, i, 0, n - 1)
    if result == None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')