# Develop a function that takes an integer <= 7 and returns a list of booleans which corresponds to the translation into binary of the parameter. Example: 5 = 101 --> [True, False, True]. Tip: try to use a dictionary to perform the translation.

# Develop a function that takes a list of integers (each integer <= 7) and returns a list of lists of booleans using the previous function.

# note: this is extremely ugly, i only did it because the excercise asked for it

def intToBin(n):
    if(n > 7):
        return "Error: number too large"
    binNumbers = {
        0: "0",
        1: "1",
        2: "10",
        3: "11",
        4: "100",
        5: "101",
        6: "110",
        7: "111"
    }
    return binNumbers[n]

def intToBinMatch(n):
    if(n > 7):
        return "Error: number too large"
    
    match n:
        case 0:
            return "0"
        case 1:
            return "1"
        case 2:
            return "10"
        case 3:
            return "11"
        case 4:
            return "100"
        case 5:
            return "101"
        case 6:
            return "110"
        case 7:
            return "111"

def intToBinList(n):
    outputList = []
    
    for c in intToBin(n):
        if(c == "1"):
            outputList.append(True)
        else:
            outputList.append(False)
    return outputList

def main():
    print("the binary representation of 5 is ", intToBin(5))
    print("the binary representation of 5 with a match case is ", intToBinMatch(5))
    print("The binary representation of 5 as a list is ", intToBinList(5))

if __name__ == "__main__":
    main()