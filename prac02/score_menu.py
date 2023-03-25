MENU="""(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""

def main():
    print(MENU)
    choice = ""

    while choice != "Q":
        choice = input("Choose one of the following option ").upper()
        if choice == "G":
            score = int(input("Enter score: "))

        elif choice == "P":
            print(determine_status(score))

        elif choice=="S":
            print(show_stars(score))

        else:
            print("Farewell")
        print(MENU)

def determine_status(score):
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
    """str(stars)=("*" * int(score)"""
    stars="*" * score
    return stars

main()
