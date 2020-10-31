# Your task is to write a function maskify, which changes all but the last four characters into '#'.


def maskify(cc):
    rev = cc[::-1]
    new_text = ''
    x = 0

    while x < len(rev):
        if x >= 4:
            new_text += '#'
        else:
            new_text += rev[x]
        x += 1
    return new_text[::-1] 


print(maskify("4556364607935616")) # == "############5616"