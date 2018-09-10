# PROGRAM : Python program for randomizing a String / Jumble_Word
# CODED BY : Suman Gangopadhyay
# DATE OF CODING : 10-Sept-2018
# CAVEATS : Using Python 3.5.2
# Email ID : linuxgurusuman@gmail.com

import random
def Jumble_Word(word):    
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

print(Jumble_Word('SumanGangopadhyay'))
