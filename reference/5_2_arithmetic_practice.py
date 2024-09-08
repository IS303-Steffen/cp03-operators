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


# PRACTICE 1: 
''' Imagine you're a teacher, and you have a jar of candies
    that you want to distribute equally among your students.
    Candies can't be cut, you can only give whole candies.

    Scenario:

    You have 47 candies.
    You have 8 students.
    You want to know how many candies each student will get
    if they are distributed evenly.

    Make variables representing the number of candies
    and the number of students.
    Print out how many candies each student can get '''


iCandy = 47
iStudent = 8
# use floor division to end up with integer 
iCandyPerStudent = iCandy // iStudent
print(iCandyPerStudent)

# Practice 2:
''' The exact same scenario as practice 1, but print out
    how many candies you will have left after distributing the candies
    out equally among the 8 students.   '''

# use modulus to get remainder
iCandyLeftOvers = iCandy % iStudent
print(iCandyLeftOvers)