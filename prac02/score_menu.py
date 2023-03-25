MENU="""(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""
HIGHEST_SCORE = 100
LOWEST_SCORE = 0

def main():
    print(MENU)
    choice = ""

    while choice != "Q":
        choice = input("Choose one of the following option ").upper()
        if choice == "G":
            score = get_valid_input("Enter score:", HIGHEST_SCORE, LOWEST_SCORE)

        elif choice == "P":
            print(determine_grade(score))

        elif choice == "S":
            print(show_stars(score))

        else:
            print("Invalid choice")
        print(MENU)
    print("Farewell")


def get_valid_input(prompt, high, low):
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid score")
        number = int(input(prompt))
    return number


def determine_grade(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    stars="*" * score
    return stars


main()