def smash(words):
    sentences = ""
    i = 0
    while i < len(words):
        sentences += words[i]
        i+=1
        if i < len(words):
            sentences += " "
    return sentences

print(smash(['hello', 'world', 'this', 'is', 'great']))