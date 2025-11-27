books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10
}

book_name = input("Enter book name: ")

while True:
    copies = input("How many copies do you want? ")
    
    if copies.isdigit():
        copies = int(copies)
        break
    else:
        print("Please enter a valid number.")

if book_name not in books:
    print("Unavailable")
else:
    if books[book_name] >= copies:
        print("Available")
    elif books[book_name] < copies:
        print("Partially Available")

