MENU="""(G)et score\n(P)rint result\n(S)how stars\n(Q)uit: """

def main():
    score = float(input("Enter score: "))
    print(determine_grades(score))

def determine_grades(score):
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
    print("*" * score)

main()
