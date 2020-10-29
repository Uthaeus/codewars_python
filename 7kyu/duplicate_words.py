# Your task is to remove all consecutive duplicate words from string, leaving only first words entries. For example:


def remove_consecutive_duplicates(s):
    result = []
    arr = s.split(" ")

    for word in arr:
        if len(result) < 1 or word != result[-1]:
            result.append(word)

    return " ".join(result)

print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta')) #, 'alpha beta gamma delta alpha beta gamma delta'