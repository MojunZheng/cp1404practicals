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



