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

# Comparisons
# Often bad in real life but very useful in programming!

'''
    >	iNum1 > iNum2   Greater Than
    <	iNum1 < iNum2	Less Than
    >=	iNum1 >= iNum2	Greater Than or Equal to
    <=	iNum1 <= iNum2	Less Than or Equal to
    !=	iNum1 != iNum2	Not Equal to
    ==	iNum1 == iNum2	Equal to (remember = is assignment, == is a comparison)
'''
# These are much more useful in Chapter 6

# But you can get simple true / false statements from them.
# Whenever you use a comparison, think of it as a function and the output
# is a boolean (True or False)
x = 10
y = 11

print (x < y)

# sometimes you want to manipulate the variables before comparing them.
# example with letters
ex1 = 'a'
ex2 = 'A'

# lowercase and uppercase are different
print(ex1 == ex2)

# You can use the upper (or lower) function to transform the output.
print(ex1.upper())
print(ex2.upper())

# Note, this doesn't change the original values of the variables:
print("this is still false")
print("comparison with original variables", ex1 == ex2)

print("but this will be true")
print("comparison with variables with the function", ex1.upper() == ex2.upper())

# PRACTICE
# check if 10 is not equal to 5 + 5
print(10 != 5+5)

