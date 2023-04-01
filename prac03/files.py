"""1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it. Remember to close your file.
Ans:
name = input("Please enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)


2.(In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
with open("name.txt", "r") as file:
    name = file.read().strip()
print("Your name is", name)



3.Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
17
42
400
with open("numbers.txt", "w") as file:
    file.write("17\n42\n400\n")


4. Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.
with open("numbers.txt", "r") as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
print(num1 + num2)


5. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers."""
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line.strip())
print(total)
