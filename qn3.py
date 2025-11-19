word = input("Enter a word: ")
index = int(input("Enter starting index: "))

substring = word[index:]
print("Substring from index", index, ":", '"' + substring + '"')
