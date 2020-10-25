string = "_________"
cell_h = [[string[x + 3 * y] for x in range(3)] for y in range(3)]
x_win = ['X', 'X', 'X']
o_win = ['O', 'O', 'O']
cell_v = []
cell_d = []
player = True


def recalculate_matrix(cell):
    global cell_h
    global cell_v
    global cell_d
    global string
    string = "".join(cell[0]+cell[1]+cell[2])
    cell_h = [[string[x + 3 * y] for x in range(3)] for y in range(3)]
    cell_v = [[string[x + 3 * y] for y in range(3)] for x in range(3)]
    cell_d = [[cell_h[x][x] for x in range(3)]] + [[cell_h[x][2 - x] for x in range(3)]]


def game(lines):

    if x_win in lines:
        print("X wins")
        return True
    elif o_win in lines:
        print("O wins")
        return True
    elif string.count('X') + string.count('O') < 9:
        pass
    else:
        print("Draw")
        return True


print(f"""---------
| {cell_h[0][0]} {cell_h[0][1]} {cell_h[0][2]} |
| {cell_h[1][0]} {cell_h[1][1]} {cell_h[1][2]} |
| {cell_h[2][0]} {cell_h[2][1]} {cell_h[2][2]} |
---------""")

while not game(cell_v + cell_h + cell_d):
    coordinate = input("Enter the coordinates: ").split()

    if len(coordinate) != 2 or not coordinate[0].isdigit() and not coordinate[1].isdigit():
        print("You should enter numbers!")
    elif int(coordinate[0]) not in list(range(1, 4)) or int(coordinate[1]) not in list(range(1, 4)):
        print("Coordinates should be from 1 to 3!")
    elif cell_h[abs(int(coordinate[1]) - 3)][int(coordinate[0]) - 1] != "_":
        print("This cell is occupied! Choose another one!")
    else:
        cell_h[abs(int(coordinate[1]) - 3)][int(coordinate[0]) - 1] = "X" if player else "O"
        print(f"""---------
| {cell_h[0][0]} {cell_h[0][1]} {cell_h[0][2]} |
| {cell_h[1][0]} {cell_h[1][1]} {cell_h[1][2]} |
| {cell_h[2][0]} {cell_h[2][1]} {cell_h[2][2]} |
---------""")
        player = not player
        recalculate_matrix(cell_h)
