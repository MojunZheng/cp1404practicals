class Guitar:
    """Create a Guitar class"""
    def __init__(self, name="", year=0, cost=0.00):
        """Initializes a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a formatted string of the guitar"""
        return f"{self.name} ({self.year}): ${self.cost:2f}"