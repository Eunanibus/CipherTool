__author__ = "Eunan Camilleri"
__copyright__ = "Copyright 2016, University of Kent"
__version__ = "1.0"
__email__ = "ec368@kent.ac.uk"
__status__ = "Development"

import src.utilities.utility as util

class CaesarCipher():

    key = int
    originaltext = str
    plaintext = str
    ciphertext = str


    def __init__(self):
        self.start()

    def decrypt(self):
        self.ciphertext = util.enterCipherText()
        self.key = 1

        while(self.key < len(util.alphabet())):
                decryptedLine = list()
                for letter in self.ciphertext.lower():
                    if(letter != " "):
                        decryptedLine.append(util.alphabet()[self.getNextIndex(letter)])
                    else:
                        decryptedLine.append(" ")

                    #Present the result
                    spacer = ""
                    if(self.key < 10) : spacer = " "
                util.regularMessage("Key: " + str(self.key) + spacer + "    DECRYPTION:  " + ''.join(decryptedLine))
                self.key += 1

    def encrypt(self):
        self.key = util.enterKey()
        while(not self.validateKey()):
            self.key = util.enterKey()
        self.plaintext = util.enterPlainTextMessage()
        while(not self.validatePlainText()):
            self.plaintext = util.enterPlainTextMessage()
        self.originaltext = self.plaintext
        self.plaintext = str(self.plaintext).lower()

        self.ciphertext = ""
        for letter in self.plaintext:
            if(not letter == " "):
                self.ciphertext += util.alphabet()[self.getNextIndex(letter)]
            else:
                self.ciphertext += " "
        util.regularMessage("'" + str(self.originaltext).upper() + "' has been encoded as: " + str(self.ciphertext).upper() + "\nWith the Key: " + str(self.key))

    def getNextIndex(self, letter):
        nextIndex = util.alphabet().index(letter) - int(self.key)
        if (nextIndex < 0):
            nextIndex = len(util.alphabet()) + (util.alphabet().index(letter) - int(self.key))
        return nextIndex



    def validateKey(self):
        if not (util.isNumeric(self.key) and int(self.key) > 0 and int(self.key) <= 26):
            util.regularMessage("\nA key for Caeser Cipher can only be numeric from 1-26. Please enter a key that fits this criteria\n")
            return False
        else:
            return True

    def validatePlainText(self):
        if not util.isAlpha(self.plaintext):
            util.regularMessage("\nCaesar cipher can only encode ASCII Text (A-Z) characters. Please enter a valid plaintext to encrypt")
            return False
        else:
            return True

    def start(self):
        util.barsMessage("caeѕar cιpнer decrypтor")
        if util.taskIsEncrypt() :
            self.encrypt()
        else:
            self.decrypt()
