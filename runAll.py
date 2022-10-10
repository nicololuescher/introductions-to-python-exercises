import introductionExcercises.calculateDisc
import introductionExcercises.flattenList
import introductionExcercises.getBiggestValue
import introductionExcercises.inserIntoOrderedList
import introductionExcercises.insertionSort
import introductionExcercises.isodd
import introductionExcercises.lengthOfString
import introductionExcercises.reverseList
import introductionExcercises.sumOfIntegers

print(
    "The area of a disc with radius 5 is",
    introductionExcercises.calculateDisc.getArea(5),
    "\n",
)

inputList = [[1, 2, 3], [4, 5, 6], [7, 8, [9, "test", 11]]]
print("list: ", inputList)
print(
    "the flattened list is",
    introductionExcercises.flattenList.flattenList(inputList),
    "\n",
)

inputList = [1, 2, 3, 40, 5, 6, 7, 8, 9, 10]
print("list: ", inputList)
print(
    "The biggest value in the list is",
    introductionExcercises.getBiggestValue.getBiggestValue(inputList),
    "\n",
)

inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("inserting", 4, "in the list", inputList)
print(
    "The list is",
    introductionExcercises.inserIntoOrderedList.insertIntoList(inputList, 4),
    "\n",
)

unorderedList = [4, 2, 8, 3, 10, 7, 1, 9, 5, 6]
print("unordered list: ", unorderedList)
orderedList = introductionExcercises.insertionSort.insertionSort(unorderedList)
print("The ordered list is", orderedList)
print("The ordered list is", orderedList, "\n")

if introductionExcercises.isodd.isOdd(5):
    print("5 is odd\n")
else:
    print("5 is even\n")
z
inputList = ["this", "is", "a", "list", "of", "strings"]
print("The list is: ", inputList)
print(
    "the length of the words in the list ",
    inputList,
    "is",
    introductionExcercises.lengthOfString.calculateLength(inputList),
    "\n",
)

inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list is: ", inputList)
print("The iterative reversed list is", introductionExcercises.reverseList.reverseIterative(inputList))
print("The recursive reversed list is", introductionExcercises.reverseList.reverseRecursive(inputList), "\n")

print("iterative sum form 1 to 10 is", introductionExcercises.sumOfIntegers.sumIterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("recursive sum from 1 to 10 is", introductionExcercises.sumOfIntegers.sumRecursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))