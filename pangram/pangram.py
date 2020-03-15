def is_pangram(sentence):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for letter in sentence.lower():
        if letter in letters:
            letters.remove(letter)

    if len(letters) == 0:
        return True
    else:
        return False
