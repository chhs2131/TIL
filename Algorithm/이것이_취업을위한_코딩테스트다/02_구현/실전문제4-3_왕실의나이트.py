input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    # 보드판 내에 위치할 수 있는 경우에 카운트
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
