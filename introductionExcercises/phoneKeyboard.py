# Develop a class that simulates the keyboard of a phone.
# Digits that are pressed are stored in the phone via a method press() until a signal is received to dial the number. Add a key backspace to be able to erase one digit and another key clear to clear the digits already stored.  A phone number should have at least 10 digits before dialing the number.

class PhoneKeyboard:
    def __init__(self):
        self.phoneNumber = []
    
    def press(self, n):
        if(type(n) == int and n >= 0 and n <= 9):
            self.phoneNumber.append(n)
    
    def backspace(self):
        self.phoneNumber.pop()
    
    def clear(self):
        self.phoneNumber = []
    
    def dial(self):
        if(len(self.phoneNumber) == 10):
            print("dialing", self.phoneNumber)
        else:
            print("invalid number")
    
    def interactive():
        print

t = PhoneKeyboard()