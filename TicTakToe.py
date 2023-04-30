import numpy as np
import random
import time
import pandas as pd

# global variables

arr = np.zeros((3, 3))
x1, x2, x3, x4, x5, x6, x7, x8, x9 = " "," ", " ", " ", " ", " ", " ", " ", " ",

board = x1 + "|"+ x2 + "|" + x3 +"\n-+-+-\n" + x4 + "|" + x5 + "|" + x6 + "\n-+-+-\n" + x7 + "|" + x8 + "|" + x9

count = 1

list1 = []
list_player1 = []
list_player2 = []

p1 = 0
p2 = 0
tie = 0

AI_score = 0

# functions required for the Game

def show_cells():
    print("Positions are as follows: ")
    print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n")

def check_value(x):
    if 1 <= x <= 9:
        return True
    else:
        return False

def check_replacement(x):
    global x1, x2, x3, x4, x5, x6, x7, x8, x9

    if x == 1 and x1 == " ":
        return True
    elif x == 2 and x2 == " ":
        return True
    elif x == 3 and x3 == " ":
        return True
    elif x == 4 and x4 == " ":
        return True
    elif x == 5 and x5 == " ":
        return True
    elif x == 6 and x6 == " ":
        return True
    elif x == 7 and x7 == " ":
        return True
    elif x == 8 and x8 == " ":
        return True
    elif x == 9 and x9 == " ":
        return True
    else:
        return False

def insert_position(x, count):
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, board

    if count % 2 != 0:
        # X - Player 1
        if x == 1:
            x1 = "X"
        elif x == 2:
            x2 = "X"
        elif x == 3:
            x3 = "X"
        elif x == 4:
            x4 = "X"
        elif x == 5:
            x5 = "X"
        elif x == 6:
            x6 = "X"
        elif x == 7:
            x7 = "X"
        elif x == 8:
            x8 = "X"
        else:
            x9 = "X"
    else:
        # O - Player 2
        if x == 1:
            x1 = "O"
        elif x == 2:
            x2 = "O"
        elif x == 3:
            x3 = "O"
        elif x == 4:
            x4 = "O"
        elif x == 5:
            x5 = "O"
        elif x == 6:
            x6 = "O"
        elif x == 7:
            x7 = "O"
        elif x == 8:
            x8 = "O"
        else:
            x9 = "O"

    board = x1 + str("|") + x2 + str(
        "|") + x3 + "\n-+-+-\n" + x4 + "|" + x5 + "|" + x6 + "\n-+-+-\n" + x7 + "|" + x8 + "|" + x9

    return board

def check_winner():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, arr, p1, p2, AI_score

    # change grid to numerical values in array

    if x1 == "X":
        arr[0][0] = 1
    elif x1 == "O":
        arr[0][0] = 10
    if x2 == "X":
        arr[0][1] = 1
    elif x2 == "O":
        arr[0][1] = 10
    if x3 == "X":
        arr[0][2] = 1
    elif x3 == "O":
        arr[0][2] = 10

    if x4 == "X":
        arr[1][0] = 1
    elif x4 == "O":
        arr[1][0] = 10
    if x5 == "X":
        arr[1][1] = 1
    elif x5 == "O":
        arr[1][1] = 10
    if x6 == "X":
        arr[1][2] = 1
    elif x6 == "O":
        arr[1][2] = 10

    if x7 == "X":
        arr[2][0] = 1
    elif x7 == "O":
        arr[2][0] = 10
    if x8 == "X":
        arr[2][1] = 1
    elif x8 == "O":
        arr[2][1] = 10
    if x9 == "X":
        arr[2][2] = 1
    elif x9 == "O":
        arr[2][2] = 10

    # checking who wins

    values = [first_line(arr), second_line(arr), third_line(arr),
              first_down(arr), second_down(arr), third_down(arr),
              dia_right(arr), dia_left(arr)]

    if 3 in values:
        print("Congratulations! Player 1 one has won. ")
        p1 += 1 # for bot bot stats
        AI_score = 1 #only used for AI training data
        return True
    elif 30 in values:
        print("Congratulations! Player 2 has won. ")
        p2 += 1 # for bot bot stats
        AI_score = -1 #only unsed for AI training data
        return True

def check_tie():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, tie, AI_score

    values = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

    if " " not in values:
        print("You both loose. You're in a tie. ")
        tie += 1
        AI_score = 0
        return True

def global_variables():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, arr, list1
    x1, x2, x3, x4, x5, x6, x7, x8, x9 = " ", " ", " ", " ", " ", " ", " ", " ", " ",
    arr = np.zeros((3, 3))
    list1 = []
# functions to find three next to each other
def first_line(arr):
    return sum(arr[0])
def second_line(arr):
    return sum(arr[1])
def third_line(arr):
    return sum(arr[2])
def first_down(arr):
    return arr[0][0] + arr[1][0] + arr[2][0]
def second_down(arr):
    return arr[0][1] + arr[1][1] + arr[2][1]
def third_down(arr):
    return arr[0][2] + arr[1][2] + arr[2][2]
def dia_right(arr):
    return arr[0][0] + arr[1][1] + arr[2][2]
def dia_left(arr):
    return arr[2][0] + arr[1][1] + arr[0][2]


# functions required for MiniMax-Algorithm

def free_cells(arr):
    # finding empty cells and saving their array coordinates in list of lists

    global list1

    list1 = []

    for i in range(len(arr)):
        for j in range(len(arr)):

            if arr[i][j] == 0:
                list1.append([i, j])

    return list1

def cells_player1(arr):
    global list_player1

    list_player1 = []

    for i in range(len(arr)):
        for j in range(len(arr)):

            if arr[i][j] == 1:
                list1.append([i, j])

    return list_player1

def cells_player2(arr):
    global list_player2

    list_player2 = []

    for i in range(len(arr)):
        for j in range(len(arr)):

            if arr[i][j] == 10:
                list1.append([i, j])

    return list_player2

# checking area around your values for possible move
def win_next_move(count, arr):
    # for the first player - player X / 1

    if count % 2 != 0:

        for value in free_cells(arr):
            i, j = value[0], value[1]  # every value are two coordinates of used cells of player 1

            arr[i][j] = 1  # going to every empty cell

            if first_line(arr) == 3:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if second_line(arr) == 3:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if third_line(arr) == 3:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if first_down(arr) == 3:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if second_down(arr) == 3:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if third_down(arr) == 3:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if dia_right(arr) == 3:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if dia_left(arr) == 3:
                arr[i][j] = 0  # setting it back to initial value
                return value

            arr[i][j] = 0  # setting it back to initial value


    # for the second player - player O / 10

    else:
        for value in free_cells(arr):
            i, j = value[0], value[1]  # every value are two coordinates of used cells of player 1

            arr[i][j] = 10  # going to every empty cell

            if first_line(arr) == 30:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if second_line(arr) == 30:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if third_line(arr) == 30:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if first_down(arr) == 30:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if second_down(arr) == 30:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if third_down(arr) == 30:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if dia_right(arr) == 30:
                arr[i][j] = 0  # setting it back to initial value
                return value
            if dia_left(arr) == 30:
                arr[i][j] = 0  # setting it back to initial value
                return value

            arr[i][j] = 0  # setting it back to initial value

def move_converter(i, j):
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, board, count, arr

    # for the first player - player X / 1

    if count % 2 != 0:

        if i == 0 and j == 0:
            x1 = "X"
            arr[0][0] = 1
        elif i == 0 and j == 1:
            x2 = "X"
            arr[0][1] = 1
        elif i == 0 and j == 2:
            x3 = "X"
            arr[0][2] = 1
        elif i == 1 and j == 0:
            x4 = "X"
            arr[1][0] = 1
        elif i == 1 and j == 1:
            x5 = "X"
            arr[1][1] = 1
        elif i == 1 and j == 2:
            x6 = "X"
            arr[1][2] = 1
        elif i == 2 and j == 0:
            x7 = "X"
            arr[2][0] = 1
        elif i == 2 and j == 1:
            x8 = "X"
            arr[2][1] = 1
        elif i == 2 and j == 2:
            x9 = "X"
            arr[2][2] = 1


    # for the second player - player O / 10

    else:
        if i == 0 and j == 0:
            x1 = "O"
            arr[0][0] = 10
        elif i == 0 and j == 1:
            x2 = "O"
            arr[0][1] = 10
        elif i == 0 and j == 2:
            x3 = "O"
            arr[0][2] = 10
        elif i == 1 and j == 0:
            x4 = "O"
            arr[1][0] = 10
        elif i == 1 and j == 1:
            x5 = "O"
            arr[1][1] = 10
        elif i == 1 and j == 2:
            x6 = "O"
            arr[1][2] = 10
        elif i == 2 and j == 0:
            x7 = "O"
            arr[2][0] = 10
        elif i == 2 and j == 1:
            x8 = "O"
            arr[2][1] = 10
        elif i == 2 and j == 2:
            x9 = "O"
            arr[2][2] = 10

    board = x1 + str("|") + x2 + str(
        "|") + x3 + "\n-+-+-\n" + x4 + "|" + x5 + "|" + x6 + "\n-+-+-\n" + x7 + "|" + x8 + "|" + x9

def find_next(arr, count):  # function to find the best spot next to an already set cell
    global list_player1, list_player2, list1, first_line, second_line, third_line, first_down, second_down, third_down, dia_right, dia_left

    list_player1 = cells_player1(arr)
    list_player2 = cells_player2(arr)
    list1 = free_cells(arr)
    possibilities = []
    first_line_items = [[0, 0], [0, 1], [0, 2]]
    second_line_items = [[1, 0], [1, 1], [1, 2]]
    third_line_items = [[2, 0], [2, 1], [2, 2]]
    first_down_items = [[0, 0], [1, 0], [2, 0]]
    second_down_items = [[0, 1], [1, 1], [2, 1]]
    third_down_items = [[0, 2], [1, 2], [2, 2]]
    dia_right_items = [[0, 0], [1, 1], [2, 2]]
    dia_left_items = [[0, 2], [1, 1], [2, 0]]

    # for the first player - player X / 1

    if count % 2 != 0:

        if first_line(arr) == 1:
            for elem in first_line_items:
                if elem in list1:
                    possibilities.append(elem)
        if second_line(arr) == 1:
            for elem in second_line_items:
                if elem in list1:
                    possibilities.append(elem)
        if third_line(arr) == 1:
            for elem in third_line_items:
                if elem in list1:
                    possibilities.append(elem)
        if first_down(arr) == 1:
            for elem in first_down_items:
                if elem in list1:
                    possibilities.append(elem)
        if second_down(arr) == 1:
            for elem in second_down_items:
                if elem in list1:
                    possibilities.append(elem)
        if third_down(arr) == 1:
            for elem in third_down_items:
                if elem in list1:
                    possibilities.append(elem)
        if dia_right(arr) == 1:
            for elem in dia_right_items:
                if elem in list1:
                    possibilities.append(elem)
        if dia_left(arr) == 1:
            for elem in dia_left_items:
                if elem in list1:
                    possibilities.append(elem)

    # for the second player - player O / 10
    else:

        if first_line(arr) == 10:
            for elem in first_line_items:
                if elem in list1:
                    possibilities.append(elem)
        if second_line(arr) == 10:
            for elem in second_line_items:
                if elem in list1:
                    possibilities.append(elem)
        if third_line(arr) == 10:
            for elem in third_line_items:
                if elem in list1:
                    possibilities.append(elem)
        if first_down(arr) == 10:
            for elem in first_down_items:
                if elem in list1:
                    possibilities.append(elem)
        if second_down(arr) == 10:
            for elem in second_down_items:
                if elem in list1:
                    possibilities.append(elem)
        if third_down(arr) == 10:
            for elem in third_down_items:
                if elem in list1:
                    possibilities.append(elem)
        if dia_right(arr) == 10:
            for elem in dia_right_items:
                if elem in list1:
                    possibilities.append(elem)
        if dia_left(arr) == 10:
            for elem in dia_left_items:
                if elem in list1:
                    possibilities.append(elem)

    # now the list possibilities has every cell next to ur existing previous moves

    try:
        length = len(possibilities) - 1
        random_cell = random.randint(0, length)
        val = possibilities[random_cell]
    except:
        val = None

    return val

def find_corner(arr, count, free):  # fucntion to find an empty corner in the beginning

    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
    possibilities = []  # to go to
    choices = []  # possibility to go and to fill the whole row

    first_line_items = [[0, 0], [0, 1], [0, 2]]
    second_line_items = [[1, 0], [1, 1], [1, 2]]
    third_line_items = [[2, 0], [2, 1], [2, 2]]
    first_down_items = [[0, 0], [1, 0], [2, 0]]
    second_down_items = [[0, 1], [1, 1], [2, 1]]
    third_down_items = [[0, 2], [1, 2], [2, 2]]
    dia_right_items = [[0, 0], [1, 1], [2, 2]]
    dia_left_items = [[0, 2], [1, 1], [2, 0]]

    for elem in corners:
        if elem in free:
            possibilities.append(elem)

    for elem in possibilities:
        if elem in first_line_items and first_line(arr) == 0:
            if elem not in choices:  # to avoid redundant values
                choices.append(elem)
        if elem in second_line_items and second_line(arr) == 0:
            if elem not in choices:
                choices.append(elem)
        if elem in third_line_items and third_line(arr) == 0:
            if elem not in choices:
                choices.append(elem)
        if elem in first_down_items and first_down(arr) == 0:
            if elem not in choices:
                choices.append(elem)
        if elem in second_down_items and second_down(arr) == 0:
            if elem not in choices:
                choices.append(elem)
        if elem in third_down_items and third_down(arr) == 0:
            if elem not in choices:
                choices.append(elem)
        if elem in dia_right_items and dia_right(arr) == 0:
            if elem not in choices:
                choices.append(elem)
        if elem in dia_left_items and dia_left(arr) == 0:
            if elem not in choices:
                choices.append(elem)

    try:
        length = len(choices) - 1
        random_cell = random.randint(0, length)
        val = choices[random_cell]
    except:
        val = None

    return val

def random_choice(free):
    random_cell = random.randint(0, len(free)-1)
    return free[random_cell]

def show_move(move):
    if move == [0, 0]:
        return 1
    elif move == [0, 1]:
        return 2
    elif move == [0, 2]:
        return 3
    elif move == [1, 0]:
        return 4
    elif move == [1, 1]:
        return 5
    elif move == [1, 2]:
        return 6
    elif move == [2, 0]:
        return 7
    elif move == [2, 1]:
        return 8
    elif move == [2, 2]:
        return 9


# Whole game

def GAME_Human_Human():
    count = 1
    global_variables()
    show_cells()

    while True:
        if count % 2 != 0:
            x = int(input("Player 1, choose your position for X: "))

            if check_value(x) and check_replacement(x):
                print(insert_position(x, count))
            else:
                continue

        else:
            x = int(input("Player 2, choose your position for O: "))

            if check_value(x) and check_replacement(x):
                print(insert_position(x, count))
            else:
                continue

        if check_winner():
            break

        if check_tie():
            break

        count += 1

def GAME_Bot_Human():
    count = 1
    global_variables()
    show_cells()

    while True:
        if count % 2 != 0:

            # start = time.time()

            free = free_cells(arr)

            if win_next_move(count, arr) is not None:

                move = win_next_move(count, arr)
                move_converter(move[0], move[1])

            elif win_next_move(count + 1, arr) is not None:

                move = win_next_move(count + 1, arr)
                move_converter(move[0], move[1])
                # count is increased by one inside of the function
                # means that the function is checking for the other player
                # can the other player win with one move, the bot will block it

            elif find_next(arr, count) is not None:

                move = find_next(arr, count)
                move_converter(move[0], move[1])

                # function finds next cells in ur started row and
                # selects a random one out of the selection

            elif find_corner(arr, count, free) is not None:

                move = find_corner(arr, count, free)
                move_converter(move[0], move[1])

                # function finds a corner which is free and
                # where it is possible to get 3 in a row from

            else:
                move = random_choice(free)
                move_converter(move[0], move[1])

            show = show_move(move)

            print("Bot, choose your position for X: " + str(show))
            # print(str(time.time()-start)+" seconds")
            print(board)


        else:
            x = int(input("Human, choose your position for O: "))

            if check_value(x) and check_replacement(x):
                print(insert_position(x, count))
            else:
                continue

        if check_winner():
            break

        if check_tie():
            break

        count += 1

def GAME_Human_Bot():
    global count
    count = 1
    global_variables()
    show_cells()

    while True:
        if count % 2 != 0:

            x = int(input("Human, choose your position for X: "))

            if check_value(x) and check_replacement(x):
                print(insert_position(x, count))
            else:
                continue


        else:
            # start = time.time()

            free = free_cells(arr)

            if win_next_move(count, arr) is not None:

                move = win_next_move(count, arr)
                move_converter(move[0], move[1])

            elif win_next_move(count + 1, arr) is not None:

                move = win_next_move(count + 1, arr)
                move_converter(move[0], move[1])
                # count is increased by one inside of the function
                # means that the function is checking for the other player
                # can the other player win with one move, the bot will block it

            elif find_next(arr, count) is not None:

                move = find_next(arr, count)
                move_converter(move[0], move[1])

                # function finds next cells in ur started row and
                # selects a random one out of the selection

            elif find_corner(arr, count, free) is not None:

                move = find_corner(arr, count, free)
                move_converter(move[0], move[1])

                # function finds a corner which is free and
                # where it is possible to get 3 in a row from

            else:
                move = random_choice(free)
                move_converter(move[0], move[1])

            show = show_move(move)

            print("Bot, choose your position for O: " + str(show))
            # print(str(time.time()-start)+" seconds")
            print(board)

        if check_winner():
            break

        if check_tie():
            break

        count += 1

def GAME_Bot_Bot():
    global count
    count = 1
    global_variables()
    show_cells()

    while True:
        if count % 2 != 0:

            # start = time.time()

            free = free_cells(arr)

            if win_next_move(count, arr) is not None:

                move = win_next_move(count, arr)
                move_converter(move[0], move[1])

            elif win_next_move(count + 1, arr) is not None:

                move = win_next_move(count + 1, arr)
                move_converter(move[0], move[1])
                # count is increased by one inside of the function
                # means that the function is checking for the other player
                # can the other player win with one move, the bot will block it

            elif find_next(arr, count) is not None:

                move = find_next(arr, count)
                move_converter(move[0], move[1])

                # function finds next cells in ur started row and
                # selects a random one out of the selection

            elif find_corner(arr, count, free) is not None:

                move = find_corner(arr, count, free)
                move_converter(move[0], move[1])

                # function finds a corner which is free and
                # where it is possible to get 3 in a row from

            else:
                move = random_choice(free)
                move_converter(move[0], move[1])

            show = show_move(move)

            print("Bot, choose your position for X: " + str(show))
            # print(str(time.time()-start)+" seconds")
            print(board)
            print(arr)



        else:

            # start = time.time()

            free = free_cells(arr)

            if win_next_move(count, arr) is not None:

                move = win_next_move(count, arr)

                move_converter(move[0], move[1])


            elif win_next_move(count + 1, arr) is not None:

                move = win_next_move(count + 1, arr)

                move_converter(move[0], move[1])

                # count is increased by one inside of the function

                # means that the function is checking for the other player

                # can the other player win with one move, the bot will block it


            elif find_next(arr, count) is not None:

                move = find_next(arr, count)

                move_converter(move[0], move[1])

                # function finds next cells in ur started row and

                # selects a random one out of the selection


            elif find_corner(arr, count, free) is not None:

                move = find_corner(arr, count, free)

                move_converter(move[0], move[1])

                # function finds a corner which is free and

                # where it is possible to get 3 in a row from


            else:

                move = random_choice(free)

                move_converter(move[0], move[1])

            show = show_move(move)

            print("Bot, choose your position for O: " + str(show))

            # print(str(time.time()-start)+" seconds")

            print(board)
            print(arr)

        if check_winner():
            break

        if check_tie():
            break

        count += 1

def GAME_Bot_Bot_AI_data():
    global count, data
    count = 1
    global_variables()
    #show_cells()
    data_part = np.zeros((3,27))
    #data_count = 0

    while True:
        if count % 2 != 0:
            # start = time.time()
            free = free_cells(arr)
            if win_next_move(count, arr) is not None:
                move = win_next_move(count, arr)
                move_converter(move[0], move[1])
            elif win_next_move(count + 1, arr) is not None:
                move = win_next_move(count + 1, arr)
                move_converter(move[0], move[1])
                # count is increased by one inside of the function
                # means that the function is checking for the other player
                # can the other player win with one move, the bot will block it
            elif find_next(arr, count) is not None:
                move = find_next(arr, count)
                move_converter(move[0], move[1])
                # function finds next cells in ur started row and
                # selects a random one out of the selection
            elif find_corner(arr, count, free) is not None:
                move = find_corner(arr, count, free)
                move_converter(move[0], move[1])
                # function finds a corner which is free and
                # where it is possible to get 3 in a row from
            else:
                move = random_choice(free)
                move_converter(move[0], move[1])

            show = show_move(move)
            #print("Bot, choose your position for X: " + str(show))
            # print(str(time.time()-start)+" seconds")
            #print(board)
            print(arr)

        else:
            # start = time.time()
            free = free_cells(arr)
            if win_next_move(count, arr) is not None:
                move = win_next_move(count, arr)
                move_converter(move[0], move[1])
            elif win_next_move(count + 1, arr) is not None:
                move = win_next_move(count + 1, arr)
                move_converter(move[0], move[1])
                # count is increased by one inside of the function
                # means that the function is checking for the other player
                # can the other player win with one move, the bot will block it
            elif find_next(arr, count) is not None:
                move = find_next(arr, count)
                move_converter(move[0], move[1])
                # function finds next cells in ur started row and
                # selects a random one out of the selection
            elif find_corner(arr, count, free) is not None:
                move = find_corner(arr, count, free)
                move_converter(move[0], move[1])
                # function finds a corner which is free and
                # where it is possible to get 3 in a row from
            else:
                move = random_choice(free)
                move_converter(move[0], move[1])
            show = show_move(move)
            #print("Bot, choose your position for O: " + str(show))
            # print(str(time.time()-start)+" seconds")
            #print(board)
            print(arr)

        # collecting data for training set
        # one 3 by 27 data block
        for i in range(3):
            for j in range(3):
                data_part[i][j+(count-1)*3] = arr[i][j]

        if check_winner():
            break
        if check_tie():
            break
        count += 1
        #data_dount += 1

    return data_part

def gaining_data(how_many_times):
    data = np.zeros((how_many_times * 3, 27))
    scores = np.zeros((how_many_times, 1))

    for i in range(how_many_times):
        data_part = GAME_Bot_Bot_AI_data()

        scores[i][0] = AI_score

        for j in range(3):
            for k in range(27):
                data[j + 3 * i][k] = data_part[j][k]

    moves_data = pd.DataFrame(data)
    scores_data = pd.DataFrame(scores)

    # moves_data.to_csv("Moves.csv")
    # scores_data.to_csv("Scores.csv")



#GAME_Human_Human()
#GAME_Bot_Human()
GAME_Human_Bot()
#GAME_Bot_Bot()
#gaining_data(10000)