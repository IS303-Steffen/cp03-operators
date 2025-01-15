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

# ===============================
# PRACTICE - ARITHEMTIC OPERATORS
# ===============================


# PRACTICE 1: 
'''
Imagine you're a teacher, and you have a jar of candies that you want to
distribute equally among your students. Candies can't be cut, you can only
give whole candies.

Scenario:

You have 47 candies.
You have 8 students.

You want to know how many candies each student will get if they are
distributed evenly.

Make variables representing the number of candies and the number of students.
Print out how many candies each student can get
'''


candy = 47
student = 8
# use floor division to end up with integer 
candy_per_student = candy // student
print(candy_per_student)

# PRACTICE 2:
'''
Use the exact same scenario as practice 1, but print out how many candies you
will have left after distributing the candies out equally among the 8 students.
'''
candy_left_over = candy % student # use modulus to find remainder.
print(candy_left_over)