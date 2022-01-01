#!/usr/bin/env python3

from constraint import *

# Each cell in the puzzle is assigned a letter from a-i arranged like so:
#
# a | b | c
# --+---+---
# d | e | f
# --+---+---
# g | h | i

problem = Problem()

cells = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Add each cell as a problem variable
for cell in cells:
    problem.addVariable(cell, possible_values)

# Add a constraint to ensure all variables are unique
problem.addConstraint(AllDifferentConstraint())

# Add circle sum constraints
problem.addConstraint(ExactSumConstraint(19), ('a', 'b', 'd', 'e'))
problem.addConstraint(ExactSumConstraint(24), ('b', 'c', 'e', 'f'))
problem.addConstraint(ExactSumConstraint(18), ('d', 'e', 'g', 'h'))
problem.addConstraint(ExactSumConstraint(27), ('e', 'f', 'h', 'i'))

# Add colour sum constraints
problem.addConstraint(ExactSumConstraint(21), ('b', 'c', 'g', 'h'))
problem.addConstraint(ExactSumConstraint(12), ('a', 'd', 'e'))
problem.addConstraint(ExactSumConstraint(12), ('f', 'i'))

# Solve it, just get the first solution if there are many
# There should only be one if the problem is constructed correctly
s = problem.getSolution()

# Print the solution in a friendly manner
print(' %d | %d | %d' % (s['a'], s['b'], s['c']))
print('---+---+---')
print(' %d | %d | %d' % (s['d'], s['e'], s['f']))
print('---+---+---')
print(' %d | %d | %d' % (s['g'], s['h'], s['i']))
