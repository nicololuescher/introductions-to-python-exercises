# Develop a function that returns True if its parameter is even, False otherwise.

import sys

def isOdd(n):
    return n % 2 == 1

def main():
    number = int(sys.argv[1]);
    if(isOdd(number)):
        print(str(number) + " is odd")
    else:
        print(str(number) + " is even")

if(__name__ == "__main__"):
    main()