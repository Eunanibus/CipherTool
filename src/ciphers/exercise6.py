import itertools
from copy import copy, deepcopy
import textwrap
import src.utilities.utility as util

class Ex:

    cipherText = "UOEEOIGOAIVYEYSTFEIHKTMOAOINUCALAEHERDAFLOIHNTWOPWAAHWOOLCAGASYFGEGDCEHEIUORAPNUUIEHRUNXOTWARRMNHCFEWEMOHOAHANEOLOWAKWEFDOENTTWTINETTOCNTFTMHDRNHHTDFSONHLTUOCETLAODILHIBSDAHHRFUAEFETDTIFOTUOEHTTHFLAHIELROELNANMWISOSDWMOOTSCCBOOEENYNEUAEWAOTEHAGTWRTSOTHALEFOOHNNRCITIEUHABNUWSIRRFRAECOCESNEIBOCREOPIVNAMCERFWLNUEHSTEOTHNOHSNSSOWNBLRYFOADAHTMEAEFVBIEEUEFALEETOIHAAAMOHENSIKIHOSKAVYNCTESOTEEICNCRYHEODTWABAKAHCOTTGEBTLLEUOOODDIATHOTMGSASCHRIUSCOOOMSSESBSDIEPLCIEEYVKWBSEMRHRTFRTKKDEITEEEHTALBNTLDCAABAEIFEARNWDYASEROOHLSTIOATINESPDREREHDGIENORCHNOUEFTNGIWEHIAOECENDSPNGRFRNELTNTCSONEFIPFDOTTLUNLPUAANBTBICTEEHOGTERLEIOREKTHTOLTEHAYODOLNRLASLWTRFFIOLLPFHONCTEEIUCNILENEUNEGFDTLNHCINBATWLGHEIANDTHTGRGHAHEFRANTHEUHRATNOHEOLSIHRNSYOEFIOPPCSPFHPENTEAAUSTEUEOHOOHECARTBNVAEAVRESHEWODTICXTESFOTSBANKSETLEISETUNHNTSEPNVSOAEATTLGNOEEFOPWAHYSNEMERWVSEF"
    columns = 6
    rows = int

    def Solve(self):

        print("Initiating...")


        # Gets everything into a 2D Array
        slice = int(len(self.cipherText) / 6)
        splitStrings = textwrap.wrap(self.cipherText, slice)
        layers = [["" for x in range(self.columns)] for y in range(slice)]
        for i in range(len(splitStrings)):
            for j in range(len(splitStrings[i])):
                layers[j][i] = splitStrings[i][j]

        # Iterates for the possible combinations of columns
        for combination in set(itertools.permutations(list(range(self.columns)))):
            newAnswer = deepcopy(layers)

            answer = ""
            for row in range(len(layers)):
                for column in range(len(newAnswer[row])):
                    answer += newAnswer[row][combination[column]]
            if answer in str(util.getOriginalText()):
                print("\nCombination Found: " + str(combination) + "\n")
                print(answer)