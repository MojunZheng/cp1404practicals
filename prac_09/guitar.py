"""
CP1404/CP5632 Practical - Suggested Solution
Guitar class
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50
class Guitar:
    """Guitar class for storing details of a guitar."""

def __init__(self, name="", year=0, cost=0):
    """Initialise a Guitar."""
    self.name = name
    self.year = year
    self.cost = cost
