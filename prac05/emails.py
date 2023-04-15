"""Estimate: 50mins, Actual:40mins """
email_dictionary = {}
email = input("Email: ")

while email != "":
    user_name = "".join(email.split("@")[0].split(".")).title()
    choice_confirmation = input(f"Is your name {user_name}? (y/n)").upper()
    if choice_confirmation != "" and choice_confirmation != "Y":
        user_name = input("Name: ").title()
    email_dictionary[user_name] = email
    email = input("Email: ")

for name, email in email_dictionary.items():
    print(email)
    print(f"{name} ({email})")

