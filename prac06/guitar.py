CURRENT_YEAR=2023
VINTAGE_AGE=50

class Guitar:
    """Storing details for a guitar"""
    def __int__(self,name="",year=0, cost=0):
        "To get guitar details"
        self.name=name
        self.year=year
        self.cost=cost

    def __str__(self):
        """Return string of the guitar"""
        return f"{self.name}({self.year}):${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """This function is to check if the guitar is vintage or not"""
        return self.get_age() >= VINTAGE_AGE

    def __It__(self,other):
        """Group the guitar by the year they were released"""
        return self.year < other.year