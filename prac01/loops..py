#3
for num in range(1, 21):
    if num % 2 != 0:
        print(num, end=' ')

#3a
for num in range(0, 101, 10):
    print(num)

#3b
for num in range(20, 0, -1):
    print(num)

#3c
user_number = int(input("Enter a number: "))

for num in range(user_number):
    print("*", end="")

#3d
user_number = int(input("Enter a number: "))

for i in range(1, user_number+1):
    print("*" * i)