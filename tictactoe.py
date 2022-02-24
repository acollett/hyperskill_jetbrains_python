# user_in = input("Enter cells:").replace("_", " ")
# game starts by printing blank grid
user_in = "         "
print("---------")
for i in range(0, 9, 3):
    print(f"| {user_in[i]} {user_in[i+1]} {user_in[i+2]} |")
print("---------")

grid = [char for char in user_in]
coords = [11, 12, 13, 21, 22, 23, 31, 32, 33]

while True:
    while True:
        next_move = input("Enter coordinates:").replace(" ", "")
        if next_move.isdigit() is False:
            print("You should enter numbers!")
        elif int(next_move) not in coords:
            print("Coordinates should be from 1 to 3!")
        elif grid[coords.index(int(next_move))] == 'X' or grid[coords.index(int(next_move))] == 'O':
            print("This cell is occupied! Choose another one!")
        else:
            break

    if grid.count('X') == grid.count('O'):
        grid[coords.index(int(next_move))] = "X"
    else:
        grid[coords.index(int(next_move))] = "O"

    update_user_in = "".join(grid)
    print("---------")       # print updated grid
    for i in range(0, 9, 3):
        print(f"| {update_user_in[i]} {update_user_in[i+1]} {update_user_in[i+2]} |")
    print("---------")

    # perform check
    if abs(grid.count('X') - grid.count('O')) > 1:
        print("Impossible")
    else:
        no_of_wins = []
        for n in range(0, 6, 3):
            if grid[n] != '_' and grid[n] == grid[n+1] and grid[n+1] == grid[n+2]:
                no_of_wins.append(grid[n])
            else:
                continue
        for m in range(0, 3, 1):
            if grid[m] != '_' and grid[m] == grid[m+3] and grid[m+3] == grid[m+6]:
                no_of_wins.append(grid[m])
            else:
                continue
        if grid[0] != '_' and grid[0] == grid[4] and grid[4] == grid[8]:
            no_of_wins.append(grid[0])
        elif grid[2] != '_' and grid[2] == grid[4] and grid[4] == grid[6]:
            no_of_wins.append(grid[2])

        if no_of_wins.count('X') == 1 and no_of_wins.count('O') == 0:
            print("X wins")
            break
        elif no_of_wins.count('X') == 0 and no_of_wins.count('O') == 1:
            print("O wins")
            break
        elif grid.count('X') + grid.count('O') == 9:                                           # if it's a draw
            print("Draw")
            break
        else:
            continue
