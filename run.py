from constraint import *

problem = Problem()

cells = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for cell in cells:
    problem.addVariable(cell, [1,2,3,4,5,6,7,8,9])

for cell1 in cells:
    for cell2 in cells:
        if cell1 != cell2:
            problem.addConstraint(lambda a, b: a != b, (cell1, cell2))

problem.addConstraint(lambda a, b, c, d: a+b+c+d == 19, ('a', 'b', 'd', 'e'))
problem.addConstraint(lambda a, b, c, d: a+b+c+d == 24, ('b', 'c', 'e', 'f'))
problem.addConstraint(lambda a, b, c, d: a+b+c+d == 18, ('d', 'e', 'g', 'h'))
problem.addConstraint(lambda a, b, c, d: a+b+c+d == 27, ('e', 'f', 'h', 'i'))

problem.addConstraint(lambda a, b, c, d: a+b+c+d == 21, ('b', 'c', 'g', 'h'))
problem.addConstraint(lambda a, b, c: a+b+c == 12, ('a', 'd', 'e'))
problem.addConstraint(lambda a, b: a+b == 12, ('f', 'i'))

print(problem.getSolutions())
