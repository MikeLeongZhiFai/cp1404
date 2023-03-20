
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
score = float(input("Enter score: "))
if score < 0 or score > 100:
    message = "Invalid score"
else:
    if score > 100:
        message="Invalid score"
    elif score >= 90:
        message="Excellent"
    elif score >= 50:
        message="Passable"
    else:
        message="Bad"

print(message)