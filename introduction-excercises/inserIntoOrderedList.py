# Develop a function that inserts a number into an ordered list and returns an ordered list (ascending order). This function will be used in the next exercise.


def insertIntoList(inputList, number):
    if len(inputList) == 0:
        inputList.append(number)
        return inputList
    for i in range(len(inputList)):
        if number < inputList[i]:
            inputList.insert(i, number)
            return inputList
    inputList.append(number)
    return inputList


def main():
    inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("inserting", 4, "in the list", inputList)
    print("The list is", insertIntoList(inputList, 4))


if __name__ == "__main__":
    main()
