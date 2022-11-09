# Develop a function insertion_sort that takes an unordered list of numbers and returns an ordered list taking advantage of the previous function.


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


def insertionSort(list):
    orderedList = []
    for i in list:
        print("inserting", i, "in the list", orderedList)
        orderedList = insertIntoList(orderedList, i)
    return orderedList


def main():
    unorderedList = [4, 2, 8, 3, 10, 7, 1, 9, 5, 6]
    orderedList = insertionSort(unorderedList)
    print("The ordered list is", orderedList)


if __name__ == "__main__":
    main()
