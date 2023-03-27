"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: ValueError will occur when a numerator or denominator input cannot be converted to an integer using the int() function
2. When will a ZeroDivisionError occur?
Ans: ZeroDivisionError occur when user enters a denominator of 0 which then cause division by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans:Yes, we could change the code to avoid the possibility of a ZeroDivisionError.To prevent the ZeroDivisionError, you might add an if statement that
 checks the denominator's equality with zero before performing the division and handles this scenario separately."""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")