def to_title_case(sentence):
    words = sentence.split()
    new_words = []

    for w in words:
        new_words.append(w.capitalize())

    return " ".join(new_words)

print(to_title_case("hello world from python"))

