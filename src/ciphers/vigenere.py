__author__ = "Eunan Camilleri"
__copyright__ = "Copyright 2016, University of Kent"
__version__ = "1.0"
__email__ = "ec368@kent.ac.uk"
__status__ = "Development"

import src.utilities.utility as util

class VigenereCipher():

    alphabet =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    keyKnown = bool
    key = str
    plaintext = str
    ciphertext = str


    def __init__(self):

        util.barsMessage("vιgenere cιpнer")
        self.start()

    def encrypt(self):
        self.plaintext = str(util.enterPlainTextMessage()).lower()
        self.key = str(util.enterKey()).lower()

        encryptedText = list()
        for letterIndex in range(len(self.plaintext)):
            letter = self.plaintext[letterIndex]  # The plaintext letter
            letterAlphaIndex = self.alphabet.index(letter)  # The alphabetic index of the encrypted letter
            keyLetter = self.key[letterIndex % len(self.key)]  # The character of the Key that corresponds to this letter
            keyAlphaIndex = self.alphabet.index(keyLetter)  # The corresponding Keys alphabetic index value

            encryptedCharacterIndex = letterAlphaIndex + keyAlphaIndex # The encrypted character's index

            if encryptedCharacterIndex >= len(self.alphabet): # If the encypted character's index is greater than the length of the alphabet
                encryptedCharacterIndex = encryptedCharacterIndex%len(self.alphabet) # Then we need to wrap around the alphabet
            encryptedText.append(self.alphabet[encryptedCharacterIndex]) # We now have the correct encrypted character
        util.regularMessage(str(self.plaintext).upper() + " has been encoded as " + "" .join(encryptedText).upper() + " with the key: " + str(self.key).upper())

    def decrypt(self):
        self.ciphertext = str(util.enterCipherText()).lower()
        self.keyCheck()
        if(self.keyKnown):
            self.decryptWithKey()
        else:
            util.regularMessage("Function not yet implemented")

    def decryptWithKey(self):
        self.plaintext = ""
        for letterIndex in range(len(self.ciphertext)):
            letter = self.ciphertext[letterIndex] # The encrypted letter
            letterAlphaIndex = self.alphabet.index(letter) # The alphabetic index of the encrypted letter
            keyLetter = self.key[letterIndex % len(self.key)] # The character of the Key that corresponds to this letter
            keyAlphaIndex = self.alphabet.index(keyLetter) # The corresponding Keys alphabetic index value
            decryptedLetterIndex = letterAlphaIndex - keyAlphaIndex
            if decryptedLetterIndex < 0: # Wraparound alphabet
                decryptedLetterIndex = (len(self.alphabet) - (keyAlphaIndex - letterAlphaIndex))
            self.plaintext += self.alphabet[decryptedLetterIndex]
        util.regularMessage("Message Decypted as: \n" + str(self.plaintext).upper())

    def keyCheck(self):
        self.key = str(input("\nDo you know the Key?\nIf yes enter it now. If not, press enter\n")).lower()
        self.keyKnown = not(not self.key) # defines a global boolean that determines whether a Key was entered (and therefore known)

    def start(self):
        if util.taskIsEncrypt():
            self.encrypt()
        else:
            self.decrypt()
