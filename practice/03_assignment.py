# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

# assignment means giving a variable a value:


# remember you can update the value of the variable and use the variable on the left side too
# this means, take whatever the value of x currently is, and add 2 to it, then make x
# equal to that new number:



# Shortcuts (compound assignment)
# feel free to use them, but if you prefer not to don't worry about it.
'''
    +=	iResult += iNumber	iResult = iResult + iNumber
    -=	iResult -= iNumber	iResult = iResult - iNumber
    *=	iResult *= iNumber	iResult = iResult * iNumber
    /=	iResult /= iNumber	iResult = iResult / iNumber
    %=	iResult %= iNumber	iResult = iResult % iNumber
    **=	iResult **= iNumber	iResult = iResult ** iNumber
    //=	iResult //= iNumber	iResult = iResult // iNumber
'''

# PRACTICE
iPractice1 = 10
iPractice2 = 23
# Try making iPractice1 equal to itself multiplied by iPractice 2 using the shortcuts
# print out the result
