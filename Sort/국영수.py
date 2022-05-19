n = int(input())

students = []

for _ in range(n):
    students.append(input().split())

# 국어 점수가 감소, 영어가 증가, 수학이 감소, 이름이 사전 순으로 증가 하는 순서로 정렬
students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])