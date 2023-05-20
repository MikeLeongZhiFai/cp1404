class Band:
    """Represent a Band class"""
    def __init__(self, name=""):
        """Initialise a Band of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the Band"""
        self.musicians.append(musician)

    def __str__(self):
        """Give back an output consisting of string representation of all musicians in band, with a comma separating each one"""
        all_musician_details = self.name + ' ('
        for musician in self.musicians:
            musician_details = musician.__str__()
            all_musician_details += musician_details + ','
        all_musician_details = all_musician_details.strip(",")
        all_musician_details += ')'
        return all_musician_details

    def play(self):
        """Returns all musicians that are involved, even without instrument"""
        all_musician_playing = ""
        for musician in self.musicians:
            all_musician_playing += musician.play() + '\n'
        return all_musician_playing