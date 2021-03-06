Suko puzzle solver using constraint programming.

Consider the following (solved) Suko puzzle. The idea is to make the four numbers add up to the total in the middle, and the numbers in the coloured cells add up to the given totals on the right.

![suko](suko.png)

*Screenshot taken from https://www.transum.org/software/Puzzles/Suko.asp*

This puzzle is an easy candidate for constraint programming. Check out the solution to this example in `suko.py` which uses the [python-constraints](https://pypi.org/project/python-constraint/) library.

## Usage

The puzzle is described using a plaintext config file which looks like this:
```
b  g  g
 19 24
b  b  r
 18 27
g  g  r

12 12 21
```

Run the solver using:
```
./suko.py <config_file>
```
