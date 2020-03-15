def abbreviate(words):
     for separator in ("-", "_"):
        words = words.replace(separator, " ")
        word_list = words.split()
     return "".join(word[0].upper() for word in word_list)

