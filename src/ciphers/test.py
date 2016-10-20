import src.utilities.utility as util

class Test():
    ciphertext = "GLGMLHWATKSABINMKKRDLXGWUKNDEPCYHXCNXHQOLNYATGVKQGVMBIHKMYCIXWUUWZNZKEDXMZNZLWQQSEUNTPCMAQHJPIFHGALKTVVXLNYXHYPCJEPZKCYNDRBZLEKMLKLHBRCCABYGRXJXMMBDOIPNNKLWXIPCZKLZLMPLWGHYTEINVCIHTRQOFOHZMCVQSZONXXQUABYIBKJQWXYWNXKBVKUYTRFPGTYGHRIJYUNJEHONLNUOTJCVARSJYWQVWYOXARCVWGMTHYTBATVGTGMVGULQTPGLSSYJKMIRFGFGRJTXEZBZLIRJJZMVGHVQSZNRXVGJGRXVGGKNFZLVVIVQSZBVWENUTANKXVKBZKXJYJVQWKUMMLVQGAACMLGWWCAZGITJLOIILHKMFZEIHAKCTANGHVFRLUIFGSPXLOWZHJVQWUFYPSOJFYLVFFNRFMMIHXKXZTIDMMUWGZBDGKUJAJNZLWVQWTNCXXCUCCUNHJDDKOHZLWQWDESJNGCWEOFFXQEUWGHHRQCRVECYHRVFSTNHRGQFKMIDGKCIWCUOMLKBLOGZHCGJJYBZKICBKALZWLKVGTNCTXRXATNVGHJNKALQXCGMZKLPIEPMVUQILLGQSJVZXRUCSECIZMPMGULNTKQXVJYVEEPMZKLXHQRUWDCJGLCMYXIRGHGUAIUOXUWRLKMPKIAXMIUILXCWVONOBWEXELIMMEDUWKHJNKJQWXYAHVTXMMBAHPMKMZQZWSPCDOPZBRCLGCWPFFGAXXUHXWJNVKWGTVGMLNUOLLGLGAFYLXCWVONVGHJNJFYNMEPMOOFGBRIWWYMNXIONVZIRBRJR"
    offsetsFound = []
    minKeyLength = 4
    maxKeyLength = 9
    bestKeyLength = int
    patternTracker = {}

    def findPattern(self):

        print("\nInitiating...\n")
        identifiedPatterns = {}

        stage = 1
        interval = 3
        currentCharacterIndex = 0

        while(currentCharacterIndex <= len(self.ciphertext)):

            characterBlock = ""
            if not (currentCharacterIndex+interval > len(self.ciphertext)):
                characterRange = range(currentCharacterIndex, currentCharacterIndex+interval)

                # Assembles the word block we are currently looking at
                for character in characterRange:
                    characterBlock += self.ciphertext[character]

                # If we've already seen it, we log it
                if characterBlock in identifiedPatterns:

                    # The range of the last pattern found
                    previousRange = identifiedPatterns[characterBlock]

                     # The index of the first pattern found
                    patternOneIndex = previousRange.start
                    #The index of the second pattern found
                    patternTwoIndex = characterRange.start

                    # We find the difference, and store it
                    self.offsetsFound.append(patternTwoIndex-patternOneIndex)
                    if(interval == 3):
                        # Tracks the frequency of this particular pattern
                        self.patternTracker[characterBlock] += 1
                else:
                    identifiedPatterns[characterBlock] = characterRange
                    if(interval == 3):
                        self.patternTracker[characterBlock] = 1
                currentCharacterIndex += interval
            else:
                if stage < interval:
                    stage += 1

                else:
                    stage = 1
                    if(interval < self.maxKeyLength):
                        interval +=1
                    else:
                        break
                identifiedPatterns = {}
                currentCharacterIndex = stage - 1
        self.findBestKeyLength()
        self.divide()

    def findBestKeyLength(self):
        scores = {}
        for keyLength in range(self.minKeyLength, self.maxKeyLength, 1):
            score = 0
            for offset in self.offsetsFound:
                if(offset%keyLength == 0):
                    score += 1
            scores[keyLength] = score

        self.bestKeyLength = max(scores, key=scores.get)
        print("\nThe best key found is " + str(self.bestKeyLength) + " with a score of " + str(scores[self.bestKeyLength]) + "\n")

    def divide(self):

        rows = int(len(self.ciphertext) / self.bestKeyLength)
        if (len(self.ciphertext) % self.bestKeyLength > 0): rows += 1

        layout = [["" for x in range(self.bestKeyLength)] for y in range(rows)]

        for letter in range(len(self.ciphertext)):
            layout[int(letter/self.bestKeyLength)][int(letter%self.bestKeyLength)] = str(self.ciphertext[letter])

        for i in range(rows):
            print(layout[i])

        frequentThreeCharPattern = max(self.patternTracker, key=self.patternTracker.get)
        print("\nMost Frequent 3 Character Pattern: " + frequentThreeCharPattern + " which appears " + str(self.patternTracker[frequentThreeCharPattern]) + " times.")
        print("\n")
        guessKey = ['I', 'I', 'I', 'I']
        self.translate(layout, guessKey)



    def convert(self, letter, key):
        keyIndex = util.alphabet().index(str(key).lower())
        letterIndex = util.alphabet().index(str(letter).lower())

        value = letterIndex-keyIndex
        if(value < 0): value = len(util.alphabet()) - (keyIndex-letterIndex)
        return str(util.alphabet()[value]).upper()

    def translate(self, layout, key):
        rows = int(len(self.ciphertext) / self.bestKeyLength)
        if (len(self.ciphertext) % self.bestKeyLength > 0): rows += 1
        for row in range(rows):
            for column in range(self.bestKeyLength):
                letter = layout[row][column]
                decryptedchar = self.convert(letter, key[column])
                layout[row][column] = decryptedchar
        print("\nTRANSLATION\n")
        for row in range(rows):
            print(layout[row])

