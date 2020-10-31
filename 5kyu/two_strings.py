# Input Strings a and b: For every character in string a swap the casing of every occurrence of the same character in string b. Then do the same casing swap with the inputs reversed. Return a single string consisting of the changed version of a followed by the changed version of b. A char of a is in b regardless if it's in upper or lower case - see the testcases too.


def arrayify(s):
    result = []
    for c in s:
        result.append(c)
    return result 

def work_on_strings(a,b):
    x = 0
    a = arrayify(a)
    b = arrayify(b)

    while x < len(a):
        y = 0
        while y < len(b):
            if a[x].lower() == b[y].lower():
                b[y] = b[y].swapcase()
            y += 1
        x += 1
    x = 0
    while x < len(b):
        y = 0
        while y < len(a):
            if b[x].lower() == a[y].lower():
                a[y] = a[y].swapcase()
            y += 1
        x += 1

    return "".join(a) + "".join(b)


print(work_on_strings("abc","cde")) #, "abCCde"