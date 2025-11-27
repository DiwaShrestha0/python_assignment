words = ["apple", "banana", "apple", "orange", "banana", "banana"]

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

duplicates = {}

for word in freq:
    if freq[word] > 1:
        duplicates[word] = freq[word]

print(duplicates)

