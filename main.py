"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 28, 2022

Lauren Altomare starting: November 1st, 2022
First Submission: November 10th, 2022 1:42 PM --> fix left diagonal direction
Second Submissions: November 20th, 2022
"""

def is_empty(board):

    #uses nested for loops to run through each square of the board
    for row in range(len(board)):
        for col in range(len(board[0])):

            #determines whether the square is empty
            if board[row][col] != " ":
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    start_bound = True
    end_bound = True
    y_start, x_start = 0, 0

    if d_y == 0:
        y_start = y_end
        x_start = x_end - length * d_x + 1

    elif d_x == 0:
        x_start = x_end
        y_start = y_end - length * d_y + 1


    #diagonal moving right to left
    elif d_x == -1:
        y_start = y_end - length * d_y + 1
        x_start = x_end - length * d_x - 1


    #diagonal moving left to right
    else:
        y_start = y_end - length * d_y + 1
        x_start = x_end - length * d_x + 1


    #checks starting point of sequence

    #only moving in x direction
    if d_y == 0:

        if x_start == 0:
            start_bound = True

        elif board[y_end][x_start - d_x] != " ":
            start_bound = True
        else:
            start_bound = False


    #only moving in y direction
    elif d_x == 0:

        if y_start == 0:
            start_bound = True

        elif board[y_start - d_y][x_end] != " ":
            start_bound = True

        else:
            start_bound = False

    #moving diagonally
    else:

        if (d_x == 1 and (y_start == 0 or x_start == 0)) or (d_x == -1 and (y_start == 0 or x_start == len(board)-1)) :
            start_bound = True

        elif board[y_start - d_y][x_start - d_x] != " ":
            start_bound = True

        else:
            start_bound = False

    #checks ending point of sequence

    #only moving in x direction
    if d_y == 0:

        if x_end == len(board)-1:
            end_bound = True

        elif board[y_end][x_end + d_x] != " ":
            end_bound = True
        else:
            end_bound = False


    #only moving in y direction
    elif d_x == 0:

        if y_end == len(board)-1:
            end_bound = True

        elif board[y_end + d_y][x_end] != " ":
            end_bound = True

        else:
            end_bound = False

    #moving diagonally
    else:

        if (d_x == 1 and (y_end == len(board)-1 or x_end == len(board)-1)) or (d_x == -1 and (y_end == len(board)-1 or x_start == 0)) :
            end_bound = True

        elif board[y_end + d_y][x_end + d_x] != " ":
            end_bound = True

        else:
            end_bound = False


    if start_bound == True and end_bound == True:
        return "CLOSED"

    elif start_bound == False and end_bound == False:
        return "OPEN"

    else:
        return "SEMIOPEN"

def start_to_end(y_start, x_start, d_y, d_x, length):

    if d_y == 0:

        y_end = y_start
        x_end = x_start + length * d_x - 1

    elif d_x == 0:
        x_end = x_start
        y_end = y_start + length * d_y - 1


    #diagonal moving right to left
    elif d_x == -1:
        y_end = y_start + length * d_y - 1
        x_end = x_start + length * d_x + 1

    #diagonal moving left to right
    else:
        y_end = y_start + length * d_y - 1
        x_end = x_start + length * d_x - 1

    return [y_end, x_end]

def all_three_detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    closed_seq_count = 0
    semi_open_seq_count = 0
    seq_coords = [] #stores coordinates of the sequences in the row
    length_count = 0
    recent_x_coord = 0
    recent_y_coord = 0

    #row is vertical
    if d_x == 0:


        #finds starting coordinate and determines length
        for i in range(len(board)):

            #start of sequence at the table edge
            if i == 0 and board[i][x_start] == col:

                length_count += 1
                recent_x_coord = x_start
                recent_y_coord = i

            #start of sequence in the middle of the row
            elif board[i][x_start] == col and board[i-1][x_start] != col:
                length_count += 1
                recent_x_coord = x_start
                recent_y_coord = i

            # an element within the sequence
            elif board[i][x_start] == col:
                length_count += 1

                #adds last coordinate if it was touching the border
                if i == (len(board)-1) and length == length_count:
                    seq_coords.append([recent_y_coord, recent_x_coord])

            #end of sequence

            else:
                if length == length_count:
                    seq_coords.append([recent_y_coord, recent_x_coord])


                #resets starting coordinates within the row to continue with the loop
                recent_x_coord = 0
                recent_y_coord = 0
                length_count = 0

    #row is horizontal
    elif d_y == 0:

        #finds starting coordinate and determines length
        for i in range(len(board)):

            #start of sequence at the table edge
            if i == 0 and board[y_start][i] == col:

                length_count += 1
                recent_x_coord = i
                recent_y_coord = y_start

            #start of sequence in the middle of the row
            elif board[y_start][i] == col and board[y_start][i-1] != col:
                length_count += 1
                recent_x_coord = i
                recent_y_coord = y_start

            # an element within the sequence
            elif board[y_start][i] == col:
                length_count += 1

                #if sequence is found at the end of the board, updates the list
                if i == (len(board)-1) and length == length_count:
                    seq_coords.append([recent_y_coord, recent_x_coord])

            #end of sequence
            else:
                if length == length_count:
                    seq_coords.append([recent_y_coord, recent_x_coord])

                #resets starting coordinates within the row to continue with the loop
                recent_x_coord = 0
                recent_y_coord = 0
                length_count = 0

    #row is diagonal from right to left
    elif d_x == -1:

        #finds starting coordinate and determines length
        for i in range(len(board)- max(y_start, (7 - x_start))):

            #start of sequence at the table edge
            if i == 0 and board[y_start][x_start] == col:
                length_count += 1
                recent_x_coord = x_start
                recent_y_coord = y_start


            #start of sequence in the middle of the row
            elif board[y_start + i][x_start-i] == col and board[y_start +i-1][x_start - i + 1] != col:
                length_count += 1
                recent_x_coord = x_start - i
                recent_y_coord = y_start + i

            # an element within the sequence
            elif board[y_start + i][x_start - i] == col:
                length_count += 1

                #if sequence is found at the end of the board, updates the list
                if i == (len(board)- max(y_start, (7 - x_start)) - 1) and length == length_count:
                    seq_coords.append([recent_y_coord, recent_x_coord])

            #end of sequence
            else:
                if length == length_count:
                    seq_coords.append([recent_y_coord, recent_x_coord])

                #resets starting coordinates within the row to continue with the loop
                recent_x_coord = 0
                recent_y_coord = 0
                length_count = 0

    #row is diagonal from left to right
    else:

        #finds starting coordinate and determines length
        for i in range(len(board)- max(y_start, x_start)):

            #start of sequence at the table edge
            if i == 0 and board[y_start][x_start] == col:
                length_count += 1
                recent_x_coord = x_start
                recent_y_coord = y_start


                #start of sequence in the middle of the row
            elif board[y_start + i][x_start + i] == col and board[y_start +i-1][x_start +i-1] != col:
                length_count += 1
                recent_x_coord = x_start + i
                recent_y_coord = y_start + i

            # an element within the sequence
            elif board[y_start + i][x_start + i] == col:
                length_count += 1

                #if sequence is found at the end of the board, updates the list
                if i == (len(board)- max(y_start, x_start) - 1) and length == length_count:
                    seq_coords.append([recent_y_coord, recent_x_coord])

            #end of sequence
            else:
                if length == length_count:
                    seq_coords.append([recent_y_coord, recent_x_coord])
                #resets starting coordinates within the row to continue with the loop
                recent_x_coord = 0
                recent_y_coord = 0
                length_count = 0


    #check the type of sequence
    for i in range(len(seq_coords)):

        if is_bounded(board, start_to_end(seq_coords[i][0], seq_coords[i][1], d_y, d_x, length)[0], start_to_end(seq_coords[i][0], seq_coords[i][1], d_y, d_x, length)[1], length, d_y, d_x) == "SEMIOPEN":
            semi_open_seq_count += 1
        elif is_bounded(board, start_to_end(seq_coords[i][0], seq_coords[i][1], d_y, d_x, length)[0], start_to_end(seq_coords[i][0], seq_coords[i][1], d_y, d_x, length)[1], length, d_y, d_x) == "OPEN":
            open_seq_count += 1

        elif is_bounded(board, start_to_end(seq_coords[i][0], seq_coords[i][1], d_y, d_x, length)[0], start_to_end(seq_coords[i][0], seq_coords[i][1], d_y, d_x, length)[1], length, d_y, d_x) == "CLOSED":
            closed_seq_count += 1

    return open_seq_count, semi_open_seq_count, closed_seq_count

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    closed_seq_count = 0
    semi_open_seq_count = 0

    open_seq_count = all_three_detect_row(board, col, y_start, x_start, length, d_y, d_x)[0]
    semi_open_seq_count = all_three_detect_row(board, col, y_start, x_start, length, d_y, d_x)[1]

    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    open_seq_count = all_three_detect_rows(board, col, length)[0]
    semi_open_seq_count = all_three_detect_rows(board, col, length)[1]

    return open_seq_count, semi_open_seq_count


def all_three_detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count, closed_seq_count = 0, 0, 0

    for d in range(len(board)):
        #adding all possibilities of open sequences in the four main directions
        open_seq_count += detect_row(board, col, 0, d, length, 1, 0)[0]
        open_seq_count += detect_row(board, col, d, 0, length, 0, 1)[0]
        open_seq_count += detect_row(board, col, d, 0, length, 1, 1)[0]
        open_seq_count += detect_row(board, col, d, len(board)-1, length, 1, -1)[0]

        #for semi open sequences
        semi_open_seq_count += detect_row(board, col, 0, d, length, 1, 0)[1]
        semi_open_seq_count += detect_row(board, col, d, 0, length, 0, 1)[1]
        semi_open_seq_count += detect_row(board, col, d, 0, length, 1, 1)[1]
        semi_open_seq_count += detect_row(board, col, d, len(board)-1, length, 1, -1)[1]

        #for closed sequences
        closed_seq_count += all_three_detect_row(board, col, 0, d, length, 1, 0)[2]
        closed_seq_count += all_three_detect_row(board, col, d, 0, length, 0, 1)[2]
        closed_seq_count += all_three_detect_row(board, col, d, 0, length, 1, 1)[2]
        closed_seq_count += all_three_detect_row(board, col, d, len(board)-1, length, 1, -1)[2]

        #so as not to double count the middle diagonal
        if d != 0:
            open_seq_count += detect_row(board, col, 0, d, length, 1, 1)[0]
            open_seq_count += detect_row(board, col, 0, len(board)-1-d, length, 1, -1)[0]
            semi_open_seq_count += detect_row(board, col, 0, d, length, 1, 1)[1]
            semi_open_seq_count += detect_row(board, col, 0, len(board)-1-d, length, 1, -1)[1]
            closed_seq_count += all_three_detect_row(board, col, 0, d, length, 1, 1)[2]
            closed_seq_count += all_three_detect_row(board, col, 0, len(board)-1-d, length, 1, -1)[2]


    return open_seq_count, semi_open_seq_count, closed_seq_count

#figure out what happens if last move is last square
def search_max(board):
    best_y = 0
    best_x = 0
    current_score = 0
    last_score = 0

    for y in range(len(board)):
        for x in range(len(board[0])):

            if board[y][x] == " ":

                put_seq_on_board(board, y, x, 1, 1, 1, "b")
                last_score = current_score
                current_score = score(board)

                if current_score > last_score:

                    best_y = y
                    best_x = x

                put_seq_on_board(board, y, x, 1, 1, 1, " ")

    return best_y, best_x


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_board_full(board):

    for y in range(len(board)):
        for x in range (len(board[0])):

            if board[y][x] == " ":
                return False
    return True

def is_win(board): #account for closed sequences too

    print(all_three_detect_rows(board, "w", 5))
    if board == [['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]:
                return "Black won"
    elif board == [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']]:
                return "White won"

    elif 1 in all_three_detect_rows(board, "b", 5):
        return "Black won"

    elif 1 in all_three_detect_rows(board, "w", 5):
        print("White won")
        return "White won"

    elif is_board_full(board) == True:
        return "Draw"

    else:
        return "Continue playing"


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    play_gomoku(8)
    #test_is_bounded()
    #some_tests()
