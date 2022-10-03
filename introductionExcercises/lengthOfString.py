# Develop a function that takes a list of strings and returns a list of integers where the elements are the length of the corresponding string. Do not use any predefined functions except 'len()'. Example: lst_len(["abc", "de", "fghi"]) returns [3,2,4]


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
    print(
        "the length of the words in the list ",
        inputList,
        "is",
        calculateLength(inputList),
    )


if __name__ == "__main__":
    main()
