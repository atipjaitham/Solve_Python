moves = input().replace('AA', '').replace('BB', '').replace('CC', '')
position = 1
for move in moves:
    if move == 'A':
        if position == 2:
            position = 1
        elif position == 1:
            position = 2
    elif move == 'B':
        if position == 2:
            position = 3
        elif position == 3:
            position = 2
    elif move == 'C':
        if position == 1:
            position = 3
        elif position == 3:
            position = 1
    else:
        print("Please enter with only A, B, C")
print(position)
