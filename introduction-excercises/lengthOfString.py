def calculateLength(listOfStrings):
    outputList = []
    
    for word in listOfStrings:
        wordLength = 0
        for letter in word:
            wordLength += 1
        outputList.append(wordLength)

    return outputList

def main():
    inputList = ["this", "is", "a", "list", "of", "strings"]
    print("the length of the words in the list ", inputList, "is", calculateLength(inputList))

if(__name__ == "__main__"):
    main()