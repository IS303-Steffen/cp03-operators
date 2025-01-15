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
# COMPARISON OPERATORS
# ====================

'''
OVERVIEW
--------
Comparisons: often bad in real life but very useful in programming!

>   Greater Than
    num_1 > num_2

<   Less Than
    num_1 < num_2

>=	Greater Than or Equal to
    num_1 >= num_2	

<=	Less Than or Equal to
    num_1 <= num_2	

!=	Not Equal to
    num_1 != num_2	

==	Equal to
    num_1 == num_2

    Remember: = is for assignment, == is for comparison)

These will be much more useful once we start using if statements. But for now
we can get boolean (True/False) results from using comparison operators.

'''



# 1. COMPARISON OPERATORS WITH NUMBERS
# See whether num_1 is less than num_2, and print out the result. Try using other
# comparison operators.
num_1 = 10
num_2 = 11


# 2. COMPARISONS WITH STRINGS
# Check whether str_1 and str_2 are the same. Remember the difference between
# = and ==. 

str_1 = 'hello'
str_2 = 'HELLO'



'''
USING FUNCTIONS TO TRANSFROM DURING COMPARISONS
-----------------------------------------------
You can use string functions like .upper() and .lower() to compare strings
In a more natural way

'''

# 3. USING .upper()
# Print out the result of using .upper() on str_1


# 4. USING .upper() IN COMPARISONS
# Use .upper() on str_1 in a comparison to see if it is equal to str_2.



