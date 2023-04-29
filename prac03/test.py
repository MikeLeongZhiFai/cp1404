
email_dictionary = {}
email = input("Email: ")

while email != "":
    name = " ".join(email.split("@")[0].split(".")).title()
    choice = input(f"Is your name {name}? (Y/n) ").lower()
    if choice != "" and choice != "y":
        name = input("Name: ").title()
    email_dictionary[name] = email
    email = input("Email: ")

for email in email_dictionary.items():
    print(email)
    print(f"{email[0]} ({email[1]})")