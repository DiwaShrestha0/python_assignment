full_name = input("Enter your full name: ")

parts = full_name.split()
first_initial = parts[0][0]
last_initial = parts[-1][0]

print("Your initials are:", first_initial.upper() + "." + last_initial.upper())
