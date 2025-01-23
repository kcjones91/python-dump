password = input("Enter a password: ")


if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Strong password")
elif len(password) >= 8 and any(char.isdigit() for char in password):
    print("Somewhat strong missing upper case broski")
else:
    print("Nah you cannot create this password bro. Sorry.")