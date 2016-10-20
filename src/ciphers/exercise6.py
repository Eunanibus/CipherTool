import itertools
from copy import copy, deepcopy

class Ex:

    cipherText = "UOEEOIGOAIVYEYSTFEIHKTMOAOINUCALAEHERDAFLOIHNTWOPWAAHWOOLCAGASYFGEGDCEHEIUORAPNUUIEHRUNXOTWARRMNHCFEWEMOHOAHANEOLOWAKWEFDOENTTWTINETTOCNTFTMHDRNHHTDFSONHLTUOCETLAODILHIBSDAHHRFUAEFETDTIFOTUOEHTTHFLAHIELROELNANMWISOSDWMOOTSCCBOOEENYNEUAEWAOTEHAGTWRTSOTHALEFOOHNNRCITIEUHABNUWSIRRFRAECOCESNEIBOCREOPIVNAMCERFWLNUEHSTEOTHNOHSNSSOWNBLRYFOADAHTMEAEFVBIEEUEFALEETOIHAAAMOHENSIKIHOSKAVYNCTESOTEEICNCRYHEODTWABAKAHCOTTGEBTLLEUOOODDIATHOTMGSASCHRIUSCOOOMSSESBSDIEPLCIEEYVKWBSEMRHRTFRTKKDEITEEEHTALBNTLDCAABAEIFEARNWDYASEROOHLSTIOATINESPDREREHDGIENORCHNOUEFTNGIWEHIAOECENDSPNGRFRNELTNTCSONEFIPFDOTTLUNLPUAANBTBICTEEHOGTERLEIOREKTHTOLTEHAYODOLNRLASLWTRFFIOLLPFHONCTEEIUCNILENEUNEGFDTLNHCINBATWLGHEIANDTHTGRGHAHEFRANTHEUHRATNOHEOLSIHRNSYOEFIOPPCSPFHPENTEAAUSTEUEOHOOHECARTBNVAEAVRESHEWODTICXTESFOTSBANKSETLEISETUNHNTSEPNVSOAEATTLGNOEEFOPWAHYSNEMERWVSEF"
    columns = 4
    rows = int

    def Solve(self):
        rows = int(len(self.cipherText)/self.columns)
        if(len(self.cipherText)%self.columns > 0): rows += 1

        layers = [["" for x in range(self.columns)] for y in range(rows)]

        for letter in range(len(self.cipherText)):

            layers[int(letter/self.columns)][int(letter%self.columns)] = self.cipherText[letter]

        for row in range(rows):
            print(layers[row])

        for combination in set(itertools.permutations(list(range(self.columns)))):
            sample = deepcopy(layers)
            newAnswer = deepcopy(layers)


            for column in range(self.columns):
                for row in range(rows):
                    newAnswer[row][column] = sample[row][combination[column]]

            print("\n\nCombination: " + str(combination) + "\n")
            for row in range(rows):
                print(newAnswer[row])



