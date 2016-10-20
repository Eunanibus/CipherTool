__author__ = "Eunan Camilleri"
__copyright__ = "Copyright 2016, University of Kent"
__version__ = "1.0"
__email__ = "ec368@kent.ac.uk"
__status__ = "Development"

import string

def titleMessage(title):
    barsMessage(title)

def decoratedMessage(message):
    print("\n¸,ø¤º°`°º¤ø,¸¸,ø¤º° " + message + " °º¤ø,¸¸,ø¤º°`°º¤ø,¸\n")

def barsMessage(message):
    print("\n▁ ▂ ▄ ▅ ▆ ▇ █ " + message + " █ ▇ ▆ ▅ ▄ ▂ ▁\n")

def checkerMessage(message):
    print("\n▀▄▀▄▀▄ " + message + " ▄▀▄▀▄▀\n")

def regularMessage(message):
    print(message)

def enterPlainTextMessage():
    return input("\nEnter the plaintext you wish to encrypt\n")

def enterCipherText():
    return input("\nEnter the cipher text you wish to decrypt\n")

def enterKey():
    return input("\nEnter the Key you'd like to use\n")

def isNumeric(string):
    return(str.isnumeric(str(string)))

def isAlpha(string):
    return(str.isalpha(string))

def isAlphaNumeric(string):
    return(str.isalnum(string))

def taskIsEncrypt():
    userInput = input("Would you like to Encrypt (1) or Decrypt (2)?\n")
    if(userInput == 1 or userInput == str(1) or userInput == "Encrypt" or userInput == "encrypt"):
        return True
    else:
        return False

def alphabet():
    return list(string.ascii_lowercase)
