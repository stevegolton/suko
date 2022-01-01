#!/usr/bin/env python3

from constraint import *
from parse import parse
import argparse

# Each cell in the puzzle is assigned a letter from a-i arranged like so:
#
# a | b | c
# --+---+---
# d | e | f
# --+---+---
# g | h | i


def load_problem(filename):
    reds = []
    blues = []
    greens = []

    problem = Problem()

    cells = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Add each cell as a problem variable
    for cell in cells:
        problem.addVariable(cell, possible_values)

    with open(filename, "r") as file:
        row0 = parse('{}  {}  {}', file.readline().strip())
        circles0 = parse('{:d} {:d}', file.readline().strip())
        row1 = parse('{}  {}  {}', file.readline().strip())
        circles1 = parse('{:d} {:d}', file.readline().strip())
        row2 = parse('{}  {}  {}', file.readline().strip())
        file.readline()
        colour_sums = parse('{:d} {:d} {:d}', file.readline().strip())

    colours = [*row0, *row1, *row2]
    circles = [*circles0, *circles1]

    for name, col in zip(cells, colours):
        if col == "r":
            reds.append(name)
        elif col == "b":
            blues.append(name)
        elif col == "g":
            greens.append(name)

    # Add a constraint to ensure all variables are unique
    problem.addConstraint(AllDifferentConstraint())

    # Add circle sum constraints
    problem.addConstraint(ExactSumConstraint(circles[0]), ('a', 'b', 'd', 'e'))
    problem.addConstraint(ExactSumConstraint(circles[1]), ('b', 'c', 'e', 'f'))
    problem.addConstraint(ExactSumConstraint(circles[2]), ('d', 'e', 'g', 'h'))
    problem.addConstraint(ExactSumConstraint(circles[3]), ('e', 'f', 'h', 'i'))

    # Add colour sum constraints
    problem.addConstraint(ExactSumConstraint(colour_sums[0]), reds)
    problem.addConstraint(ExactSumConstraint(colour_sums[1]), blues)
    problem.addConstraint(ExactSumConstraint(colour_sums[2]), greens)

    return problem


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)

    args = parser.parse_args()

    # Load the problem from the passed-in filename
    problem = load_problem(args.filename)

    # Solve it, just get the first solution if there are many
    # There should only be one solution, assuming the problem is constructed correctly
    s = problem.getSolution()

    # Print the solution in a friendly manner
    print(' %d | %d | %d' % (s['a'], s['b'], s['c']))
    print('---+---+---')
    print(' %d | %d | %d' % (s['d'], s['e'], s['f']))
    print('---+---+---')
    print(' %d | %d | %d' % (s['g'], s['h'], s['i']))
