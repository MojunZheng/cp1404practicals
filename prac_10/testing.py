"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)
def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length
def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence: capital first letter, single full stop at end.
    >>> phrase_to_sentence("hello")
    'Hello.'
    >>> phrase_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> phrase_to_sentence("good morning everyone")
    'Good morning everyone.'
    """
    phrase = phrase.strip()
    # Capitalize first letter
    phrase = phrase[0].upper() + phrase[1:]
    # Ensure it ends with a single '.'
    if not phrase.endswith("."):
        phrase += "."
    return phrase
def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # assert statements to check Car fuel
    car_default = Car()
    assert car_default.fuel == 0, "Car default fuel is not 0"

    car_custom = Car(fuel=10)
    assert car_custom.fuel == 10, "Car custom fuel is not set correctly"


run_tests()
# Run doctests
doctest.testmod()
