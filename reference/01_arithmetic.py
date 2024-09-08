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


# addition: +
# add 2 and 5
print("addition", 2 + 5)

# subtraction -
# subtract 5 from 2
print("subtraction", 2 - 5)

# multiplication *
# multiply 2 and 5
print("multiplication", 2 * 5)

# division: /  
''' note this is a forward slash: /
    we used back slash before for escape characters: \ like \'
    the way I remember is that we read from left to right.
    in a forward slash it is like the line's head is leaning forward /
    in a back slash it's like the line is leaning backwards \ '''
# divide 2 by 5

print("division", 2 / 5)

# exponentiation: **
''' note, some other languages use ^ instead of **.
    That is something else entirely in python (Bitwise OR, don't worry about it)
    so don't use it for exponentiation  '''
# do 2 to the 5th
print("exponentiation", 2 ** 5)

# Modulus: %
''' modulus gives you the remainder from dividing two numbers together
    Ex. 6 / 2 evenly divides into 3, so there is 0 remaining
    But 7 / 2 doesn't evenly divides. 3 2's can fit into 7, with one left over
    so 7 % 2 would give an answer of 1. '''
# show the remainder of 10 / 2 and the remainder of 25 / 7
print("Modulus, no remainders", 10 % 2)
print("Modulus, some remainders:", 25 % 7)

#note if you use % with something bigger on the right side, it'll just give you the number
print("Modulus, big right side", 10 % 12)

# Floor Division: //
''' Same as division, but will round down to the nearest whole number
    Ex. 5 / 2 = 2.5 but 5 // 2 = 2. You can think of it chopping off the
    decimals, but just beware that if you're working with negative numbers
    it is still rounding down. try it with -5 / 2 and -5 // 2'''
# use floor division of -5 divided by 2
print("floor division", -5 //2)

