# Develop a function that transforms a list of lists into another list of lists as follows:
# [[x1,x2,x3],[y1,y2,y3], ...] --> [[x1,y1,...],[x2,y2,...],[x3,y3,...]]
# The function assumes that all the lists in the input list have the same number of elements.

def reverseMatrix(matrix):
    outputMatrix = [ [None] * len(matrix) for i1 in range(len(matrix)) ]
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            outputMatrix[y][x] = matrix[x][y]
    return outputMatrix

def main():
    print(reverseMatrix([
        ["x1", "x2", "x3"],
        ["y1", "y2", "y3"],
        ["z1", "z2", "z3"]
        ]))

if __name__ == "__main__":
    main()