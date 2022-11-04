from tracemalloc import start
import numpy as np

startPosition = 1505
endPosition = 3162


def convert(s):
    if s == b"X":
        return endPosition
    if s == b"Y":
        return startPosition
    else:
        return s


def checkDevisor(n1, n2):
    for i in range(2, max(n1, n2)):
        if n1 % i == 0 and n2 % i == 0:
            return True
    return False


def checkNeighbours(pos, grid):
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
    if grid[pos[0], pos[1]] == endPosition:
        validPaths.append(path)
        return path
    else:
        path.append(pos)
        for move in checkNeighbours(pos, grid):
            grid[pos[0], pos[1]] = -1
            makeMove(grid.copy(), move, path.copy(), validPaths)


def main():
    matrix = np.loadtxt("et.txt", dtype=int, converters=lambda s: convert(s))
    print(matrix.view())
    validPaths = []
    makeMove(matrix.copy(), [5, 5], [], validPaths)
    print("Valid Paths:")
    for path in validPaths:
        print("Path length: ", len(path))
        print(path)


if __name__ == "__main__":
    main()
