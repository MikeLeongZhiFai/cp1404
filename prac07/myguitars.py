import csv


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}): ${}".format(self.name, self.year, self.cost)

    def __lt__(self, other):
        return self.year < other.year


guitar_file = 'guitars.csv'
guitar_list = []
with open(guitar_file, 'r') as guitar_file:
    guitar_file.readline()
    for line in guitar_file:
        parts = line.strip().split(',')
        current_guitar = Guitar(parts[0], parts[1], parts[2])
        guitar_list.append(current_guitar)
    sorted_guitar_list = sorted(guitar_list)
    for guitar in sorted_guitar_list:
        print(guitar)


def new_guitar(guitar_file):
    new_guitar_name = input("Name: ")
    while new_guitar_name != "":
        new_guitar_year = input("Year: ")
        new_guitar_cost = input("Cost: $")
        add_new_guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_cost)
        guitar_list.append(add_new_guitar)
        new_guitar_name = input("Name: ")
    with open(guitar_file, 'w') as guitar_file:
        for current_guitar in guitar_list:
            guitar_file.write(current_guitar)