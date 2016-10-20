__author__ = "Eunan Camilleri"
__copyright__ = "Copyright 2016, University of Kent"
__version__ = "1.0"
__email__ = "ec368@kent.ac.uk"
__status__ = "Development"

import src.ciphers.caesar as caeser
import src.ciphers.transposition as transposition
import src.ciphers.vigenere as vignere
import src.ciphers.xor as xor
import src.utilities.utility as util
import src.ciphers.test as test
import src.ciphers.exercise6 as Ex6


class Solver(object):
    pass

    def __init__(self):
        util.decoratedMessage("welcoмe тo eυnan'ѕ encrypтιon cιpнer тool")
        print("Enter 1 for Caeser Cipher\n")
        print("Enter 2 for Vigenere Cipher\n")
        print("Enter 3 for Transposition Cipher\n")
        print("Enter 4 for XOR Cipher")
        x = input()
        if x == "1" :
            caeser.CaesarCipher()
        elif x == "2":
            vignere.VigenereCipher()
        elif x == "3":
            transposition.TranspositionCipher()
        else:
            xor.XOR()



Ex6.Ex().Solve()