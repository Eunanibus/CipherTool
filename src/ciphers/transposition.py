__author__ = "Eunan Camilleri"
__copyright__ = "Copyright 2016, University of Kent"
__version__ = "1.0"
__email__ = "ec368@kent.ac.uk"
__status__ = "Development"

import re

import src.utilities.utility as util


class TranspositionCipher():

    alphabet =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    keyKnown = bool
    key = str
    ciphertext = str
    plaintext = str


    def __init__(self):
        util.barsMessage("тranѕpoѕιтιon cιpнer decrypтor")
        self.start()

    def simpleEncrypt(self):

        self.plaintext = str(util.enterPlainTextMessage())

        counter = 1;
        oddLetters = list()
        evenLetters = list()
        for letter in self.plaintext:
            if counter % 2 == 1 :
                oddLetters.append(letter)
            else :
                evenLetters.append(letter)
            counter += 1
        print(str(self.plaintext).upper() + " has been encoded to " + '' .join(oddLetters+evenLetters).upper())

    def getAlphaNumeric(self, letter):
        return self.alphabet.index(letter)+1

    def complexEncrypt(self):

        self.plaintext = str(util.enterPlainTextMessage())
        originaltext = self.plaintext
        
        #remove any non-alphabetic characters
        regex = re.compile('[^a-zA-Z]')
        self.plaintext = regex.sub('', self.plaintext.lower())

        self.key = str(input("\nNow enter a key...\n")).lower()

        rows = int(len(self.plaintext)/len(self.key))
        if(len(self.plaintext)%len(self.key) > 0): rows += 1

        # Creates a list containing 5 lists, each of 8 items, all set to 0
        shuffledText = [["" for x in range(len(self.key))] for y in range(rows)]

        counter = 0
        values = self.getEncryptionValues()

        for counter in range(len(self.plaintext)):
            row = int(counter/len(self.key))
            column = counter%len(self.key)
            text = self.plaintext[counter]
            shuffledText[row][column] = text
            counter += 1

        textsTransposed = [["" for k in range(rows)] for l in range(len(self.key))]

        for i in range(len(self.key)):
            for j in range(rows):
                textsTransposed[(values[i])-1][j] = shuffledText[j][i]

        encryptedText = ""
        for r in range(len(self.key)):
            encryptedText += "".join(textsTransposed[r])
        print("\nThe Plaintext: '" + originaltext + "' has been encoded as: \n" + encryptedText.upper() + "\nWith the key: " + str(self.key).upper())

    def getEncryptionValues(self):

        #orderedKeyValues is a list of each character in the key sorted by alphabetical order
        orderedKeyValues = list(self.key)
        orderedKeyValues.sort()

        #the mappedIndexes dictionary keeps track of mapped letters as individuals, combatting the difficulty of duplicate letters and retrieving their indexes when the same
        mappedIndexes = {}
        indexCounter = 0
        for indexCounter in range(len(orderedKeyValues)):
            mappedIndexes[indexCounter] = False

        #for mapping KeyCharacter indexes with their sequential point value
        keyValues = [None] * len(self.key)

        #counters are used as opposed to iteration, because retrieving duplicate letters in a key will retrieve the same value.
        #for example, "GREENPEACE" would map the same letter "e" over and over. So we refer to each character by index value
        #this fully compensates for a key word with several of the same letters

        #for each character in the key
        counter = 0
        for counter in range(len(self.key)):

            #for each character in the ordered key values
            iterator = 0
            for iterator in range(len(orderedKeyValues)):

                #if the current key Character matches the current ordered Key Value, then it is the next sequential letter in the order
                if(self.key[counter] == orderedKeyValues[iterator]):

                    #if it hasn't already been mapped (for identical letters)
                    if not mappedIndexes[iterator]:

                        #then map the index of the keyCharacter with its value - KEYINDEX <=> OREDERD SEQUENTIAL VALUE
                        keyValues[counter] = iterator+1

                        #mark this character as mapped
                        mappedIndexes[iterator] = True
                        #we now don't need to continue looking for the character
                        break

                    iterator +=1
            counter+=1

        return keyValues


    def encrypt(self):
        if input("Simple (1) or Complex(2)?\n") == str(1):
            self.simpleEncrypt()
        else:
            self.complexEncrypt()

    def decrypt(self):
        print("▀▄▀▄▀▄ Enter the cipher text you wish to decrypt ▄▀▄▀▄▀\n")

    def start(self):
        if util.taskIsEncrypt():
            self.encrypt()
        else:
            self.decrypt()
