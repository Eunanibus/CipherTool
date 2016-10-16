__author__ = "Eunan Camilleri"
__copyright__ = "Copyright 2016, University of Kent"
__version__ = "1.0"
__email__ = "ec368@kent.ac.uk"
__status__ = "Development"

import src.utilities.utility as util

class CaesarCipher():

    alphabet =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    key = 1
    ciphertext = str


    def __init__(self):
        self.start()

    def decrypt(self):
        util.barsMessage("caeѕar cιpнer decrypтor")
        self.ciphertext = util.enterCipherText()
        self.key = 1

        while(self.key < len(self.alphabet)):
                decryptedLine = list()
                for letter in self.ciphertext.lower():
                    if(letter != " "):
                        nextIndex = self.alphabet.index(letter)-self.key
                        if(nextIndex < 0):
                            nextIndex = len(self.alphabet)+(self.alphabet.index(letter)-self.key)
                        decryptedLine.append(self.alphabet[nextIndex])
                    else:
                        decryptedLine.append(" ")

                    spacer = ""
                    if(self.key < 10) : spacer = " "
                print("Key: " + str(self.key) + spacer + "    DECRYPTION:  " + ''.join(decryptedLine))
                self.key += 1

    def start(self):
        if util.taskIsEncrypt() :
            print("Not yet available")
        else:
            self.decrypt()
