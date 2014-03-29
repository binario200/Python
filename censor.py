def censor(text, word):
    asterisks = "*" * len(word)
    words = text.split()
    for w in range(len(words)):
        if word == words[w]:
            words[w] = asterisks
        
    return " ".join(words)