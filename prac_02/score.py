"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """main function"""
    score = random.randint(0, 100)
    result = determine_score(score)
    print(f"Your result is {result}")


def determine_score(score):
    """Determine the level of the inputted score and return a string result."""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
