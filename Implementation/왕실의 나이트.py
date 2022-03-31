input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
    (-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2)
]

count = 0

for step in steps:
    new_row = row + step[0]
    new_column = column + step[1]

    if 1 <= new_row <= 8 and 1 <= new_column <= 8:
        count += 1

print(count) 