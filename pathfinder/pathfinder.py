from tracemalloc import start
import numpy as np

startPosition = 1505
endPosition =   3162


def convert(s):
    """helper function to convert the input file to a numpy array and replace X and Y with a given start and end position

    Args:
        s (bytes): input bytes

    Returns:
        int: integer value of the input bytes

    >>> convert(b'X')
    3162

    >>> convert(b'Y')
    1505

    >>> convert(b'15')
    15
    """
    if s == b"X":
        return endPosition
    if s == b"Y":
        return startPosition
    else:
        return int(s)


def checkDevisor(n1, n2):
    """function to check if n1 and n2 have a common devisor greater than 1

    Args:
        n1 (int): first number
        n2 (int): second number

    Returns:
        bool: True if n1 and n2 have a common devisor greater than 1

    >>> checkDevisor(2, 4)
    True

    >>> checkDevisor(2, 3)
    False
    """
    for i in range(2, max(n1, n2)):
        if n1 % i == 0 and n2 % i == 0:
            return True
    return False


def checkNeighbors(pos, grid):
    """function to get a list of valid neighbors for a given position

    Args:
        pos (list): current position
        grid (numpy.ndarray): grid to check

    Returns:
        list: list of valid neighbors

    >>> checkNeighbors([0, 0], np.array([[1, 2], [3, 4]]))
    []

    >>> checkNeighbors([0, 1], np.array([[1, 2], [3, 4]]))
    [[1, 1]]
    """
    returnList = []
    if pos[0] > 0 and checkDevisor(grid[pos[0]][pos[1]], grid[pos[0] - 1][pos[1]]):
        returnList.append([pos[0] - 1, pos[1]])

    if pos[0] < grid.shape[0] - 1 and checkDevisor(
        grid[pos[0]][pos[1]], grid[pos[0] + 1][pos[1]]
    ):
        returnList.append([pos[0] + 1, pos[1]])

    if pos[1] > 0 and checkDevisor(grid[pos[0]][pos[1]], grid[pos[0]][pos[1] - 1]):
        returnList.append([pos[0], pos[1] - 1])

    if pos[1] < grid.shape[1] - 1 and checkDevisor(
        grid[pos[0]][pos[1]], grid[pos[0]][pos[1] + 1]
    ):
        returnList.append([pos[0], pos[1] + 1])

    return returnList


def makeMove(grid, pos, outputPaths=False, path=[], validPaths=[]):
    """recursive function to make a move on the grid and check if the move is valid

    Args:
        grid (numpy.ndarray): grid to check
        pos (list): current position
        path (list): list of positions already visited
        validPaths (list): list of valid paths, used for output

    Returns:
        list: the last instance of makemove will return a list of valid paths

    >>> makeMove(np.array([[3162, 2], [3, 4]]), [1, 1])
    [[[1, 1], [0, 1]]]
    """
    if not "currentDepth" in globals():
        global currentDepth
        currentDepth = 1
        validPaths = []
        path = []
    else:
        currentDepth += 1

    if grid[pos[0], pos[1]] == endPosition:
        validPaths.append(path)
    else:
        path.append(pos)
        for move in checkNeighbors(pos, grid):
            grid[pos[0], pos[1]] = -1
            makeMove(grid.copy(), move, outputPaths, path.copy(), validPaths)
    currentDepth -= 1
    if currentDepth == 0:
        del currentDepth
        if outputPaths:
            printPaths(validPaths)
        return validPaths


def printPaths(paths):
    """Print the paths in a readable format

    Args:
        paths (list): list of valid paths

    >>> printPaths([[[1, 1], [0, 1]]])
    Valid Paths:
    Path length: 2
    [[1, 1], [0, 1]]
    """
    print("Valid Paths:")
    for path in paths:
        print("Path length:", len(path))
        print(path)


def main():
    """main function to read the input file and call the recursive function to find the valid paths"""
    makeMove(
        np.loadtxt("et.txt", dtype=int, converters=lambda s: convert(s)), [5, 5], True
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
