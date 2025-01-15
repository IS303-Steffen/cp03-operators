import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ====================
# ARITHEMTIC OPERATORS
# ====================

'''
OVERVIEW
--------
Operators are symbols that perform some action on variables or a set of 
variables (like adding them together)

Python has built-in operators for all common mathematical operations.

'''

# 1. ADDITION
# Use + to add 2 numbers together. Print out the result.
print("addition", 2 + 5)

# 2. SUBTRACTION - 
# Use - to subtract 2 numbers together. Print out the result.
print("subtraction", 2 - 5)

# 3. MULTIPLICATION
# Use * to multiply 2 numbers together. Print out the result.
print("multiplication", 2 * 5)

'''
TIP: FORWARD VS BACK SLASH
--------------------------
This is a forward slash: /
This is a back slack: \ 

We used back slash before for escape characters: \ like \'

The way I remember the difference is that we read from left to right.
In a forward slash it is like the line's head is leaning forward /
In a back slash it's like the line is leaning backwards \  
'''


# 4. DIVISION
# Use / to divide 2 numbers together Print out the results.
print("division", 2 / 5)

# 5. EXPONENTIATION
# Use ** to do a number to the xth power. Print out the results
print("exponentiation", 2 ** 5)

''' 
TIP
---
Some other languages use ^ instead of **.
That is something else entirely in python (Bitwise OR, don't worry about it)
so don't use it for exponentiation.
'''

# =======
# MODULUS
# =======

'''
A modulus operation gives you the remainder from dividing two numbers together

Ex. 6 / 2 evenly divides into 3, so there is 0 remaining

But 7 / 2 doesn't evenly divides. 3 2's can fit into 7, with one left over
so 7 % 2 would give an answer of 1.

'''

# 6. MODULUS
# Use % to show the remainder of 10 / 2 and the remainder of 25 / 7. Print out
# the results.
print("Modulus, no remainders", 10 % 2)
print("Modulus, some remainders:", 25 % 7)

'''
TIP
---
If you use % with something bigger on the right side, it'll just give you the
left side number

E.g. 10 % 12 gives you 10
    - 12 goes into 10 0 times, with 10 left over.

'''

# ==============
# FLOOR DIVISION
# ==============

# Floor Division: //
'''
Same as division, but will round down to the nearest whole number.

Ex. 5 / 2 = 2.5 but 5 // 2 = 2.

You can think of it chopping off the decimals, but just beware that if you're
working with negative numbers it is still rounding down. 

Try it with -5 / 2 and -5 // 2
'''

# FLOOR DIVISION
# Use // to find the rounded down result of dividing 2 numbers. Print the
# result.
print("floor division", -5 //2)

