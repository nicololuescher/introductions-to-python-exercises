# Develop a function that flats a list of lists without using any predefined functions. Example: flat([[3,8],[8,9,9],[1,2]]) returns [3,8,8,9,9,1,2] flat([["ab","c"],["d","ef"]]) returns ["ab","c","d","ef"]


def flattenList(input, outputList=[]):
    if type(input) == list:
        for element in input:
            flattenList(element, outputList)
    else:
        outputList.append(input)
    return outputList


def main():
    inputList = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11]]]
    print("the flattened list is", flattenList(inputList))


if __name__ == "__main__":
    main()
