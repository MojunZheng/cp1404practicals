"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""
from collections import namedtuple
import csv


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer = pointer

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, Has pointer arithmetic? {self.pointer}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def is_pointer(self):
        """Determine if language has pointer arithmetic"""
        return self.pointer == "Yes"
