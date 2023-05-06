class Project:
    def __init__(self, name, start_date, priority, cost_estimation, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimation = cost_estimation
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, Started on {self.start_date}, Priority level:{self.priority}, Estimated cost:${self.cost_estimation}, Completed amount:{self.completion_percentage}%"

    def is_complete(self):
        if self.completion_percentage == 100:
            return True
        else:
            return False