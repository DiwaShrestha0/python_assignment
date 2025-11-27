password = input("Enter a password: ")

has_letter = False
has_digit = False
has_special = False

for c in password:
    if c.isalpha():
        has_letter = True
    elif c.isdigit():
        has_digit = True
    elif c in "@#$%&":
        has_special = True

if len(password) < 6 or password.isalpha():
    print("Weak password")
elif len(password) >= 6 and has_letter and has_digit and not has_special:
    print("Moderate password")
elif len(password) >= 8 and has_letter and has_digit and has_special:
    print("Strong password")
else:
    print("Moderate password")
