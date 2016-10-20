import itertools
from copy import copy, deepcopy
import src.utilities.utility as util

class Ex:

    cipherText = "UOEEOIGOAIVYEYSTFEIHKTMOAOINUCALAEHERDAFLOIHNTWOPWAAHWOOLCAGASYFGEGDCEHEIUORAPNUUIEHRUNXOTWARRMNHCFEWEMOHOAHANEOLOWAKWEFDOENTTWTINETTOCNTFTMHDRNHHTDFSONHLTUOCETLAODILHIBSDAHHRFUAEFETDTIFOTUOEHTTHFLAHIELROELNANMWISOSDWMOOTSCCBOOEENYNEUAEWAOTEHAGTWRTSOTHALEFOOHNNRCITIEUHABNUWSIRRFRAECOCESNEIBOCREOPIVNAMCERFWLNUEHSTEOTHNOHSNSSOWNBLRYFOADAHTMEAEFVBIEEUEFALEETOIHAAAMOHENSIKIHOSKAVYNCTESOTEEICNCRYHEODTWABAKAHCOTTGEBTLLEUOOODDIATHOTMGSASCHRIUSCOOOMSSESBSDIEPLCIEEYVKWBSEMRHRTFRTKKDEITEEEHTALBNTLDCAABAEIFEARNWDYASEROOHLSTIOATINESPDREREHDGIENORCHNOUEFTNGIWEHIAOECENDSPNGRFRNELTNTCSONEFIPFDOTTLUNLPUAANBTBICTEEHOGTERLEIOREKTHTOLTEHAYODOLNRLASLWTRFFIOLLPFHONCTEEIUCNILENEUNEGFDTLNHCINBATWLGHEIANDTHTGRGHAHEFRANTHEUHRATNOHEOLSIHRNSYOEFIOPPCSPFHPENTEAAUSTEUEOHOOHECARTBNVAEAVRESHEWODTICXTESFOTSBANKSETLEISETUNHNTSEPNVSOAEATTLGNOEEFOPWAHYSNEMERWVSEF"
    columns = 6
    rows = int

    def Solve(self):

        print("Initiating...")

        #Gets everything into a 2D Array
        rows = int(len(self.cipherText)/self.columns)
        if(len(self.cipherText)%self.columns > 0): rows += 1
        layers = [["" for x in range(self.columns)] for y in range(rows)]
        for letter in range(len(self.cipherText)):
            layers[int(letter/self.columns)][int(letter%self.columns)] = self.cipherText[letter]

        # Iterates for the possible combinations of columns
        for combination in set(itertools.permutations(list(range(self.columns)))):
            newAnswer = deepcopy(layers)

            answer = ""
            for row in range(rows):
                for column in range(len(newAnswer[row])):
                    answer += newAnswer[row][combination[column]]
            print(answer)
            if answer in str(util.getOriginalText()):
                print("\nCombination Found: " + str(combination) + "\n")
                print(answer)