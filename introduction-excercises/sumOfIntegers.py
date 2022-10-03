def sumIterative(inputList):
    sum = 0
    for i in inputList:
        sum += i
    return sum

def sumRecursive(inputList, sum = 0):
    if(len(inputList) > 0):
        sum += inputList.pop()
        return sumRecursive(inputList, sum)
    else:
        return sum

def main():
    print("iterative sum form 1 to 10", sumIterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print("recursive sum from 1 to 10", sumRecursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

if(__name__ == "__main__"):
    main()