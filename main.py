grid_changed = [
    [" | ", " | ", ""],
    [" | ", " | ", ""],
    [" | ", " | ", ""]
]

new_grid = [
    ["","",""],
    ["","",""],
    ["","",""],
]
def create_board():
    grid = [
        ["  | ", "  | ", " "],
        ["----------"],
        ["  | ", "  | ", "   "],
        ["----------"],
        ["  | ", "  | ", "   "]
    ]



    for g in grid:
        print("".join(g))

def check_answer():
    global correctAnswer
    # Row Checker
    for row in new_grid:
        if "".join(x for x in row) == "XXX":
            print("X Won")
            correctAnswer = False
        if "".join(x for x in row) == "000":
            print("0 Won")
            correctAnswer = False

    # Col Checker
    for i in range(0,3):
        column = "".join(new_grid[j][i] for j in range(3))
        if column == "XXX":
            print("X Won")
            correctAnswer = False
        if column == "000":
            print("0 Won")
            correctAnswer = False

    #Dig Checker
    diagonal1 = new_grid[0][0] + new_grid[1][1] + new_grid[2][2]
    diagonal2 = new_grid[0][2] + new_grid[1][1] + new_grid[2][0]

    if diagonal1 == "XXX" or diagonal2 == "XXX":
        print("X Won")
        correctAnswer = False
    if diagonal1 == "000" or diagonal2 == "000":
        print("0 Won")
        correctAnswer = False
def make_mark():
    global counter
    if counter % 2 == 0:
        counter_value = "X"
    else:
        counter_value = "0"

    correctInput = True
    while correctInput:

        try:
            row = int(input("\nWhich Row (1-3): "))
            column = int(input("Which Column (1-3): "))
            if row <= 3 and row >= 0:
                if 3 >= column >= 0:
                    if new_grid[row-1][column-1] != "":
                        print("Type it Out Again")
                    else:
                        correctInput = False
            else:
                print("TYPE '1' or '2' or '3'")
        except ValueError:
            print("DONT TYPE TEXT")

    if column==3:
        grid_changed[row - 1][column - 1] = counter_value
        new_grid[row - 1][column - 1] = counter_value
    else:
        grid_changed[row-1][column-1] = counter_value + " | "
        new_grid[row - 1][column - 1] = counter_value


    grid_changed.insert(1,["--------"])
    grid_changed.insert(3,["--------"])
    for g in grid_changed:
        print("".join(g))
    grid_changed.remove(["--------"])
    grid_changed.remove(["--------"])
    counter = counter + 1
    check_answer()



create_board()
counter = 0
correctAnswer = True
while counter < 9 and correctAnswer:
    make_mark()

# myList = [['one', 'two', 'three'],['one', 'two', 'three'],['one', 'two', 'three']]
#
# myList.insert(1, ['zero'])
#
# myList.insert(3, ['zero'])








