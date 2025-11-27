words = ["This", "is", "good", "is"]

freq = {}

for w in words:
    w = w.lower()
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)

