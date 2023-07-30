import random
# EMPTY 4 * 4 MATRIX
def start_game():
    mat= []
    for i in range(4):
        mat.append([0]*4)
    return mat
# ADDING A 2 AT EMPTY SPACE AFTER LRUD OPERATION
def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2

# DEFINING CURRENT STATE OF THE GAME
def current_state_of_game(mat):
    # if 2048 is present anywhere THEN WON
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WON"
    # IF 0 IS PRESENT ANYWHERE
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return "GAME NOT OVER"
    # IF CONSECUTIVE SAME NUMBERS ARE PRESENT THEN THEY CAN BE COMBINED
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                return "GAME NOT OVER"
    # GAME NOT OVER FOR LAST ROW
    for j in range(3):
        if mat[3][j] ==mat[3][j+1]:
            return "GAME NOT OVER"
    # GAME NOT OVER FOR LAST COL.
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "GAME NOT OVER"
    # IF NEITHER OF THOSE IS TRUE THEN LOST
    return 'LOST'

# COMPRESSION FUNCTION : ALL THE NON ZERO VALUES COME TO ONE SIDE
'''AGAR 2 0 0 2 HAI TO USKA SEEDA 4 0 0 0 NHI KR SKTE HAIN PHLE COMPRESS KRNA HOGA LIKE 2 2 0 0 , New Matrix
me existing matrix me nhi , or return bhi newmatrix krni hai'''
def compress(mat):
    changed = False
    newmat = []
    for i in range(4):
        newmat.append([0]*4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                newmat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return newmat,changed
# MERGE FUNCTION
'''compress krne k baad consecutive left and right wale same hai to unhe merge kr denge like 2 2 0 0
or merge k baad 4 0 0 0 second place pr 0 aa jayegi'''
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j]!= 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    return mat,changed

#REVERSE FUNCTION
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            #appending elements at ith list...
            new_mat[i].append(mat[i][4-j-1])
    return new_mat

#TRANSPOSE FUNCTION
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

'''ALL POSSIBLE MOVES IN 2048'''
# MOVING LEFT
'''---------- COMPRESS THE MATRIX
--------------MERGE IT
--------------COMPRESS THE NEW MERGED MATRIX AGAIN'''
def move_left(grid):
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    return new_grid,changed

# MOVING RIGHT
'''----------REVERSE THE MATRIX
-------------COMPRESS
-------------MERGE
-------------COMPRESS
-------------REVERSE AGAIN'''
def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid,changed

# MOVING UP
'''--------TRANSPOSE THE MATRIX
-----------COMPRESS
-----------MERGE
-----------COMPRESS
-----------TRANSPOSE AGAIN'''
def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed

# MOVING DOWN
'''--------TRANSPOSE THE MATRIX
-----------REVERSE
-----------COMPRESS
-----------MERGE
-----------COMPRESS
-----------REVERSE
-----------TRANSPOSE'''
def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid,changed






