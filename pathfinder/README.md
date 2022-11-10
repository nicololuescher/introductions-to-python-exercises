# Pathfinder
@Nicolo Lüscher (luscn2)  
Repo: https://github.com/nicololuescher/introductions-to-python-exercises

This is a simple pathfinder for a 2D grid. It uses a recursive backtracking algorithm to find a path from a start to an end point. The path is then displayed in the console. This program always displays the shortest path, but can be modified to display all possible paths.

## Dependencies
- Tested with Python 3.10
- Doctest (pre-installed with Python)
- NumPy `pip install numpy` or `conda install numpy`

## Usage
- Place the `et.txt` file in the same directory as the `pathfinder.py` file.
- Run the `pathfinder.py` file.
- The path will be displayed in the console.
- Use `python3 pathfinder.py -v` to display the output of the doctests.

## Code explanation
*- Refer to the doctests in the code for more information.*  
The `pathfinder.py` file contains the following functions:
- `convert()` converts the start and end position in the `et.txt` file into a suitable integer.
- `checkDevisor()` checks if two numbers have a common divisor other than 1.
- `checkNeighbors()` returns a list of all possible moves from a given position.
- `makeMove()` is a recursive function that finds all paths from the start to the end position. It keeps track of all active function calls and returns once the last function call has been completed. It keeps track of the valid paths in a list. If the option outputPaths is set to True, it will print all valid paths.
- `printPaths()` prints the shortest path from the list of valid paths.
- `main()` is the main function that starts the program.

### TL;DR of the algorithm
The algorithm works in the following way:  
1. The doctests are run. If any of the doctests fail, the program will exit with an appropriate message.
1. The main function loads the `et.txt` file and converts the start and end position into a suitable integer. It then calls the `makeMove()` function with the grid, the start position and the outputPaths option set to True.
1. The `makeMove()` function checks if the current position is the end position. If it is, it adds the path to the list of valid paths and returns. If it is not, it checks all possible moves from the current position. If there is a valid move, it calls the `makeMove()` function again with the new position. If there are no valid moves, it returns.  
While the `makeMove()` function is running, it keeps track of all active function calls. It does this by incrementing and decrementing the `currentDepth` variable. If a function call returns, it checks if the `currentDepth` variable is 0. If it is, it means that all function calls have returned and the program can terminate. It then calls the `printPaths()` function to print the shortest path from the list of valid paths.
1. The `printPaths()` function prints the shortest path from the list of valid paths.

## Why this approach?
I think recursive algorithms are very well suited for pathfinding problems. They are easy to understand and implement. They are also very efficient. The only downside is that they can be difficult to debug. However, this is not a problem in this case, because the doctests make sure that the program works as intended.  
I've also chosen to implement a doctest for every function in the program. I need to know doctests for another module, so I have to learn them anyway.  
