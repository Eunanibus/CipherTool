__author__ = "Eunan Camilleri"
__copyright__ = "Copyright 2016, University of Kent"
__version__ = "1.0"
__email__ = "ec368@kent.ac.uk"
__status__ = "Development"

import src.utilities.utility as util

class VigenereCipher():

    # Maps the boolean context of whether the Cipher key is known
    keyKnown = bool

    # Stores the currently known key in any given context (decrypt/encrypt)
    key = str

    # Stores the plaintext
    plaintext = str

    # Stores the ciphertext
    ciphertext = str


    def __init__(self):

        util.barsMessage("vιgenere cιpнer")
        self.start()

    def encrypt(self):
        # Retrieve the plaintext and key to encrypt the text
        self.plaintext = str(util.enterPlainTextMessage()).lower()
        self.key = str(util.enterKey()).lower()

        # A list to temporarily store characters once encrypted
        encryptedText = list()

        # For every letter in the plaintext
        for letterIndex in range(len(self.plaintext)):
            letter = self.plaintext[letterIndex]  # The plaintext letter
            letterAlphaIndex = util.alphabet().index(letter)  # The alphabetic index of the encrypted letter
            keyLetter = self.key[letterIndex % len(self.key)]  # The character of the Key that corresponds to this letter
            keyAlphaIndex = util.alphabet().index(keyLetter)  # The corresponding Keys alphabetic index value

            encryptedCharacterIndex = letterAlphaIndex + keyAlphaIndex # The encrypted character's index

            if encryptedCharacterIndex >= len(util.alphabet()): # If the encypted character's index is greater than the length of the alphabet
                encryptedCharacterIndex = encryptedCharacterIndex%len(util.alphabet()) # Then we need to wrap around the alphabet
            encryptedText.append(util.alphabet()[encryptedCharacterIndex]) # We now have the correct encrypted character
        util.regularMessage(str(self.plaintext).upper() + " has been encoded as " + "" .join(encryptedText).upper() + " with the key: " + str(self.key).upper())

    def decrypt(self):
        # Retrieves the ciphertext to be decrypted (and key if known)
        self.ciphertext = str(util.enterCipherText()).lower()
        self.keyCheck()
        if(self.keyKnown):
            self.decryptWithKey()
        else:
            util.regularMessage("Function not yet implemented")

    def decryptWithKey(self):
        """Decrypts a Vigenere Cipher where the encryption key is known """

        # Initialise the plaintext storage
        self.plaintext = ""

        # For every letter in the ciphertext
        for letterIndex in range(len(self.ciphertext)):
            letter = self.ciphertext[letterIndex] # The encrypted letter
            letterAlphaIndex = util.alphabet().index(letter) # The alphabetic index of the encrypted letter
            keyLetter = self.key[letterIndex % len(self.key)] # The character of the Key that corresponds to this letter
            keyAlphaIndex = util.alphabet().index(keyLetter) # The corresponding Keys alphabetic index value
            decryptedLetterIndex = letterAlphaIndex - keyAlphaIndex
            if decryptedLetterIndex < 0: # Wraparound alphabet
                decryptedLetterIndex = (len(util.alphabet()) - (keyAlphaIndex - letterAlphaIndex))
            self.plaintext += util.alphabet()[decryptedLetterIndex]
        util.regularMessage("Message Decypted as: \n" + str(self.plaintext).upper())

    def findPattern(self):

        patternIdentified = False
        interval = 3
        buffer = {}

        while(not patternIdentified):
            for letterIndex in range(len(self.ciphertext)):
                charactersAtInterval = ""
                for characterIndex in range(letterIndex, letterIndex+interval):
                    charactersAtInterval += self.ciphertext[characterIndex]
                    letterIndex = letterIndex+interval
                    if not charactersAtInterval in buffer:
                        buffer[charactersAtInterval] = range(letterIndex, letterIndex+interval)
                    else:
                        patternIdentified = True


    def keyCheck(self):
        self.key = str(input("\nDo you know the Key?\nIf yes enter it now. If not, press enter\n")).lower()
        if self.key == "":
            self.keyKnown = False
        else:
            self.keyKnown = True

    def start(self):
        if util.taskIsEncrypt():
            self.encrypt()
        else:
            self.decrypt()
