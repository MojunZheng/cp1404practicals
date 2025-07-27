"""Musician class for CP1404"""

class Musician:
    """Musician class"""
def __init__(self, name=""):
    """Construct a Musician with a name and empty instrument collection."""
    self.name = name
    self.instruments = []
def __str__(self):
    """Return a string representation of a Musician."""
    return f"{self.name} ({self.instruments})"
def __repr__(self):
    """Return a string representation of a Musician, showing the variables."""
    return str(vars(self))
