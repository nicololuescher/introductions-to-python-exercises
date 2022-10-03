# Develop a function that returns the greatest value of a list of positive numbers.


def getBiggestValue(inputList):
    biggestValue = 0
    for i in inputList:
        if i > biggestValue:
            biggestValue = i
    return biggestValue


def main():
    inputList = [1, 2, 3, 40, 5, 6, 7, 8, 9, 10]
    print("The biggest value in the list is", getBiggestValue(inputList))


if __name__ == "__main__":
    main()
