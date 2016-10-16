__author__ = "Eunan Camilleri"
__copyright__ = "Copyright 2016, University of Kent"
__version__ = "1.0"
__email__ = "ec368@kent.ac.uk"
__status__ = "Development"

import src.utilities.utility as util

class XOR():

    alphabet =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    keyKnown = bool
    key = str
    ciphertext = str


    def __init__(self):

        util.barsMessage("хor cιpнer")
        self.start()

    def encrypt(self):
        plaintext = str(util.enterPlainTextMessage()).upper()
        binaryText = self.stringToBinary(plaintext).replace(" ", "")
        self.key = "1000100010100001110010001011010010101100"

        encryptedText = str
        counter = 0
        for counter in range(len(binaryText)):
            encryptedText += int(bool(binaryText[counter] != self.key[counter]))

        return encryptedText



        # for letter in plaintext:
        #     letterIndex = self.alphabet.index(letter)
        #     keyIndex = plaintext.index(letter)%len(self.key)
        #     keyValue = self.alphabet.index(self.key[keyIndex])
        #     encryptedCharacterIndex = letterIndex-keyValue
        #     if encryptedCharacterIndex < 0:
        #         encryptedCharacterIndex = len(self.alphabet)-(keyValue-letterIndex)
        #     encryptedText.append(self.alphabet[encryptedCharacterIndex])
        # print("\n" + str(plaintext).upper() + " has been encoded as " + "" .join(encryptedText).upper() + " with the key: " + str(self.key).upper())

    def decrypt(self):
        self.ciphertext = str(util.enterCipherText())
        util.enterPlainTextMessage("Function not yet availabe")

    def keyCheck(self):
        self.key = input("\nDo you know the Key?\nIf yes enter it now. If not, press enter")
        self.keyKnown = not self.key

    def stringToBinary(self, text):
        binaryOutput = ' '.join(format(ord(x), 'b') for x in text)
        return binaryOutput

    def start(self):
        if util.taskIsEncrypt():
            self.encrypt()
        else:
            self.decrypt()
