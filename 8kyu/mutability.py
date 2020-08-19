

def capitalize_word(word):
    pre = word[0]
    post = word[1:]

    newWord = pre.upper() + post 

    return newWord


print(capitalize_word('word')) #, 'Word')
print(capitalize_word('i')) #, 'I')