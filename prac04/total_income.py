def main():
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_record(incomes)


def print_record(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(len(incomes)):
        income = incomes[month]
        total += income
        print("Month {:<2} - Income: ${:10.2f} Total: ${:10.2f}".format(month + 1, income, total))


main()