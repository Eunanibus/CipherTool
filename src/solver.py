__author__ = "Eunan Camilleri"
__copyright__ = "Copyright 2016, University of Kent"
__version__ = "1.0"
__email__ = "ec368@kent.ac.uk"
__status__ = "Development"

import src.ciphers.caesar as caeser
import src.ciphers.transposition as transposition
import src.ciphers.vigenere as vignere
import src.utilities.utility as util


class Solver(object):
    pass

    def __init__(self):
        util.decoratedMessage("welcoмe тo eυnan'ѕ encrypтιon cιpнer тool")
        print("Enter 1 for Caeser Cipher\n")
        print("Enter 2 for Vigenere Cipher\n")
        print("Enter 3 for Transposition Cipher\n")
        x = input()
        if x == "1" :
            caeser.CaesarCipher()
        elif x == "2":
            vignere.VigenereCipher()
        else :
            transposition.TranspositionCipher()


Solver()