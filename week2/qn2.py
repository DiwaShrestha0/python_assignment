text = input("Enter a sentence: ")
words = text.split()
new_words = []

for i in range(len(words)):
    if i % 2 == 1:
        new_words.append(words[i][::-1])
    else:
        new_words.append(words[i])

result = " ".join(new_words)
print(result)

