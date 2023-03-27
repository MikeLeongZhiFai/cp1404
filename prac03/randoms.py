import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
Ans:Smallest is 5, largest is 20

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
Ans: No, line 2 could not produce a 4 because the code is suppose to print a random odd integer between 3 and 9.

What did you see on line 3?
What was the smallest number you could have seen, what was the largest? 
Ans:Smallest is 2.5 and largest is 5.5
Write code, not a comment, to produce a random number between 1 and 100 inclusive.  """


random_number=random.randint(1,100)
print(random_number)