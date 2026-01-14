from helper_functions import clear_screen
clear_screen()

# ====================
# ASSIGNMENT OPERATORS
# ====================

'''
OVERVIEW
--------
Assignment means putting a value in a variable. We use the = for this, but it
does NOT mean equality like in mathematics. For equality, we use another
operator shown in the next section.

The = sign just means put whatever is on the right side into the left side.

store_here = put everything here into the left.

'''

# 1. ASSIGNMENT
# Create a variable and assign it the value of 5. Print it out.
x = 5
print(x)


# 2. ASSIGNING A NEW VALUE BASED ON THE OLD VALUE
# Using the same variable you created above, set a new value equal to the 
# current value + 2.

x = x + 2
print(x)

# ================================
# COMPOUND ASSIGNMENTS (SHORTCUTS)
# ================================

'''
+=
    result += number	result = result + number
-=
    result -= number	result = result - number
*=
    result *= number	result = result * number
/=
    result /= number	result = result / number
%=
    result %= number	result = result % number
**=
    result **= number	result = result ** number
//=
    result //= number	result = result // number
'''

# 3. SHORTCUT ASSIGNMENT
# Use += to make example_num equal to itself plus example_num_2. Print the 
# result.
example_num = 10
example_num_2 = 3


# 4. SHORTCUT ASSIGNMENT
# Use *= to make example_num equal to itself times example_num_2. Print the 
# result.
