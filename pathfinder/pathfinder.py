from tracemalloc import start
import numpy as np
import doctest

startPosition = 1505
endPosition = 3162


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


def checkNeighbours(pos, grid):
    """function to get a list of valid neighbours for a given position
    
    Args:
        pos (list): current position
        grid (numpy.ndarray): grid to check
    
    Returns:
        list: list of valid neighbours
    
    >>> checkNeighbours([0, 0], np.array([[1, 2], [3, 4]]))
    []
    
    >>> checkNeighbours([0, 1], np.array([[1, 2], [3, 4]]))
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


def makeMove(grid, pos, path, validPaths):
    """recursive function to make a move on the grid and check if the move is valid

    Args:
        grid (numpy.ndarray): grid to check
        pos (list): current position
        path (list): list of positions already visited
        validPaths (list): list of valid paths, used for output

    Returns:
        bool: True if path is valid
    
    >>> makeMove(np.array([[endPosition, 2], [3, 4]]), [0, 0], [], [])
    True
    """
    if grid[pos[0], pos[1]] == endPosition:
        validPaths.append(path)
        return True
    else:
        path.append(pos)
        for move in checkNeighbours(pos, grid):
            grid[pos[0], pos[1]] = -1
            makeMove(grid.copy(), move, path.copy(), validPaths)


def main():
    """main function to read the input file and call the recursive function to find the valid paths
    >>> main()
    Valid Paths:
    Path length:  30
    [[5, 5], [4, 5], [3, 5], [2, 5], [2, 6], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [6, 6], [7, 6], [7, 5], [7, 4], [7, 3], [6, 3], [5, 3], [5, 2], [6, 2], [6, 1], [5, 1], [4, 1], [4, 2], [4, 3], [3, 3], [3, 4], [2, 4], [1, 4], [1, 3], [2, 3]]
    Path length:  30
    [[5, 5], [4, 5], [3, 5], [2, 5], [2, 6], [2, 7], [3, 7], [4, 7], [5, 7], [5, 6], [6, 6], [7, 6], [7, 5], [7, 4], [7, 3], [6, 3], [5, 3], [5, 2], [6, 2], [6, 1], [5, 1], [4, 1], [4, 2], [4, 3], [3, 3], [3, 4], [2, 4], [1, 4], [1, 3], [2, 3]]
    Path length:  18
    [[5, 5], [6, 5], [6, 4], [6, 3], [5, 3], [5, 2], [6, 2], [6, 1], [5, 1], [4, 1], [4, 2], [4, 3], [3, 3], [3, 4], [2, 4], [1, 4], [1, 3], [2, 3]]
    Path length:  22
    [[5, 5], [5, 6], [6, 6], [7, 6], [7, 5], [7, 4], [7, 3], [6, 3], [5, 3], [5, 2], [6, 2], [6, 1], [5, 1], [4, 1], [4, 2], [4, 3], [3, 3], [3, 4], [2, 4], [1, 4], [1, 3], [2, 3]]
    Path length:  24
    [[5, 5], [5, 6], [5, 7], [6, 7], [6, 6], [7, 6], [7, 5], [7, 4], [7, 3], [6, 3], [5, 3], [5, 2], [6, 2], [6, 1], [5, 1], [4, 1], [4, 2], [4, 3], [3, 3], [3, 4], [2, 4], [1, 4], [1, 3], [2, 3]]
    """
    matrix = np.loadtxt("et.txt", dtype=int, converters=lambda s: convert(s))
    validPaths = []
    makeMove(matrix.copy(), [5, 5], [], validPaths)
    print("Valid Paths:")
    for path in validPaths:
        print("Path length: ", len(path))
        print(path)


if __name__ == "__main__":
    doctest.testmod()
    main()
