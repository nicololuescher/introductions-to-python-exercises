import introductionExcercises.calculateDisc
import introductionExcercises.car
import introductionExcercises.flattenList
import introductionExcercises.getBiggestValue
import introductionExcercises.inserIntoOrderedList
import introductionExcercises.intToBinDictionary
import introductionExcercises.insertionSort
import introductionExcercises.isodd
import introductionExcercises.lengthOfString
import introductionExcercises.phoneKeyboard
import introductionExcercises.removeMinMax
import introductionExcercises.reverseList
import introductionExcercises.reverseMatrix
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
print("recursive sum from 1 to 10 is", introductionExcercises.sumOfIntegers.sumRecursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "\n")

print("the binary representation of 5 is ", introductionExcercises.intToBinDictionary.intToBin(5))
print("the binary representation of 5 with a match case is ", introductionExcercises.intToBinDictionary.intToBinMatch(5))
print("The binary representation of 5 as a list is ", introductionExcercises.intToBinDictionary.intToBinList(5), "\n")

print("The iversion of ['x1', 'x2', 'x3'], ['y1', 'y2', 'y3'], ['z1', 'z2', 'z3']] is: ", introductionExcercises.reverseMatrix.reverseMatrix([["x1", "x2", "x3"],["y1", "y2", "y3"], ["z1", "z2", "z3"]]), "\n")

print("After removing the lowest and highest entries in the dictionary {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}, the dictionary looks like this: ", introductionExcercises.removeMinMax.removeMinMax({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}), "\n")

print("creating new phone keyboard")
t = introductionExcercises.phoneKeyboard.PhoneKeyboard()

print("dialing number 079 123 4567")
t.press(0)
t.press(7)
t.press(9)
t.press(1)
t.press(2)
t.press(3)
t.press(4)
t.press(5)
t.press(6)
t.press(7)

print("starting call")
print(t.phoneNumber)
t.dial()
print("\n")

print("creating a car with a consumtion of 6.5l/100km and a tank size of 30l and then drive it for 100km")
car = introductionExcercises.car.Car(6.5, 30)
car.fill()
car.drive(100)
print("Fuel level after driving 100km:", car.checkFuelLevel(), "\n")