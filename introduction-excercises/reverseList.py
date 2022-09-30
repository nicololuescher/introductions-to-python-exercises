# Develop a function that reverses a list of elements (try to develop an iterative and a recursive solution).

def reverseIterative(inputList):
    outputList = []
    for i in inputList:
        outputList.insert(0, i)
    return outputList

def reverseRecursive(inputList):
    if(len(inputList) == 0):
        return []
    else:
        # return the last element of the list and the recursive call of the function with the list without the last element
        return [inputList[-1]] + reverseRecursive(inputList[:-1])

def main():
    inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("The iterative reversed list is", reverseIterative(inputList))
    print("The recursive reversed list is", reverseRecursive(inputList))

if(__name__ == "__main__"):
    main()