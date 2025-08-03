"""
CP1404/CP5632 Practical
Recursion
"""

def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# TODO 1: Write down what you think the output of this will be.
# I think do_it(5) counts how many odd numbers are between 1 and 5.
# Because n % 2 is 1 for odd numbers and 0 for even numbers.
# For 5,4,3,2,1 the remainders are 1,0,1,0,1.
# So total should be 3.

# TODO 2: Use the debugger to step through and see what's actually happening.
print(do_it(5))  # The output is 3, which matches my guess.

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        print(n ** 2)
    do_something(n - 1)

# TODO 3: Write down what you think the output of do_something(4) will be.
# I think it should print 16, 9, 4, 1, 0 — squares of 4 down to 0.

# TODO 4: Use the debugger to step through and see what's actually happening.
# The original function causes infinite recursion and crashes because there is no base case.

# do_something(4)  # Uncommenting this causes error because of infinite recursion.

# TODO 5: Fix do_something() so that it works according to the docstring.
def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return  # Base case: stop recursion
    print(n ** 2)
    do_something(n - 1)

# Now test the fixed function
do_something(4)
