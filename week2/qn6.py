def largest_word(sentence):
    words = sentence.split()
    largest = words[0]

    for word in words:
        if len(word) > len(largest):
            largest = word

    return largest

print(largest_word("Python programming is awesome"))

