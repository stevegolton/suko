from constraint import *

# Each cell in the puzzle is assigned a letter from a-i arranged like so:
#
# a | b | c
# --+---+---
# d | e | f
# --+---+---
# g | h | i

problem = Problem()

rows = cols = 6

cells = range(0, rows * cols)
possible_values = [' ', '║', '═', '╔', '╗', '╚', '╝']
# possible_values = range(0, 6)

def track_count(vals, desired):
    count = 0
    for v in vals:
        if v != ' ':
            count += 1
    
    return count == desired


def constrain_row(problem, row, desired_sum):
    vs = range(row * cols, row * cols + rows)
    problem.addConstraint(lambda *args: track_count(args, desired_sum), vs)


def constrain_col(problem, col, desired_sum):
    vs = range(col, rows*cols, cols)
    problem.addConstraint(lambda *args: track_count(args, desired_sum), vs)


# Add each cell as a problem variable
for cell in cells:
    problem.addVariable(cell, possible_values)

constrain_row(problem, 0, 3)
constrain_row(problem, 1, 3)
constrain_row(problem, 2, 2)
constrain_row(problem, 3, 3)
constrain_row(problem, 4, 4)
constrain_row(problem, 5, 2)

constrain_col(problem, 0, 1)
constrain_col(problem, 1, 2)
constrain_col(problem, 2, 4)
constrain_col(problem, 3, 4)
constrain_col(problem, 4, 3)
constrain_col(problem, 5, 3)
# constrain_col(problem, 1, 3)
# constrain_col(problem, 2, 1)

s = problem.getSolution()

for y in range(rows):
    for x in range(cols):
        print(s[x + y * cols], end='')
    print()

lut = {
    0: ' ',
    1: '║',
    1: '═',
    2: '╔',
    3: '╗',
    4: '╚',
    5: '╝',
}
