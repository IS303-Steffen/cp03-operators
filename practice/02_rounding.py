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

# ========
# ROUNDING
# ========

'''
OVERVIEW
--------
You can use the round() function to round floats to a specific decimal point.
Technically, this isn't an operator, but it is included in your textbook's
operators chapter, so we'll briefly mention it here.

SYNTAX
------

round(number, decimal_place)

'''
example_num = 107.8456
# 1. ROUNDING, DECIMAL POINTS
# Use the round() function to round example_num to the 3rd decimal place. Print


# 2. ROUNDING, WHOLE NUMBER
# Use the round() function to round example_num to a whole number. Print the 
# result.


# 3. ROUNDING, LEFT OF THE DECIMAL
# Use the round() function with a negative 2nd argument to round to the 10s
# place. Print the result.


# 4. ROUNDING FROM .5
# Try rounding odd_num and even_num to a whole number and print out each.
# What's going on?
odd_num = 1.5
even_num = 2.5


# 5. ROUNDING FROM .5 AGAIN
# See the example numbers below. Try trounding to the 1st decimal and print
# each out.

odd_num_2 = 1.65
even_num_2 = 2.75


'''
TIP: BANKERS ROUNDING, UNEXPECTED BEHAVIOR
------------------------------------------
If you are rounding a number from .5 as the last decimal, if the number
preceding .5 is odd it will round up, if the preceding .5 is even it will
round down.

Why do this?

TL;DR: Always rounding from .5 means on average you round up more than you
round down. Bankers Rounding gets around this.

Bias Reduction:
Traditional rounding (always rounding .5 up) can introduce an
upward bias over large datasets, whereas bankers' rounding tends to reduce this
bias by distributing half-roundings evenly between up and down.

Fairness:
In situations like financial transactions where rounding can benefit or
penalize a party, bankers' rounding is seen as more neutral and fair.

Statistical Robustness:
Over large datasets, bankers' rounding helps in reducing the cumulative error,
making statistical results slightly more robust.

Prevents Encouraging Unwanted Behavior:
In certain contexts, if rounding always goes up, it might encourage behaviors
like always setting prices just a half unit lower than a full number to take
advantage of the rounding.

'''
