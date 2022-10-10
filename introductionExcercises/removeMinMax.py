# Develop a function that takes a dictionary  as parameter and returns another dictionary without both the elememts (key, value) that correspond to the maximum and minimum values of the dictionary parameter.

def removeMinMax(dict):
    min = 9**99
    max = -1
    output = {}
    
    for key in dict:
        if(dict[key] > max):
            max = dict[key]
        if(dict[key] < min):
            min = dict[key]
    
    for key in dict:
        if(dict[key] != max and dict[key] != min):
            output[key] = dict[key]
    
    return output
        

def main():
    print("After removing the lowest and highest entries in the dictionary {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}, the dictionary looks like this: ", removeMinMax({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}))

if __name__ == "__main__":
    main()