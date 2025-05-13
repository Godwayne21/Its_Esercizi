from enum import *

class Genere (StrEnum):
    uomo = auto()
    donna = auto()

print (__name__)


if __name__ == 'main':

    print (Genere.uomo)
    print (Genere.donna)