MAXIMUM_PERCENTAGE = 100

class Project:
    """Create a project class"""

    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage = percentage
