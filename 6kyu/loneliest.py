# Complete the function which accepts a string and return an array of character(s) that have the most spaces to their right and left.


def loneliest(strng):
    new_str = strng.strip()
    longest = 0
    obj = {}
    pre = 0
    post = 0
    current_char = ''
    x = 0
    result = []

    while x < len(new_str):
        if x == 0:
            current_char = new_str[x]
        elif new_str[x] == ' ':
            pre += 1
        elif new_str[x] != ' ':
            if pre + post > longest:
                longest = pre + post 
            obj[current_char] = pre + post 
            current_char = new_str[x]
            post = pre 
            pre = 0
        obj[current_char] = pre + post 
        if pre + post > longest:
            longest = pre + post 
        x += 1
    print (obj)

    for i in obj:
        if obj[i] == longest:
            result.append(i)

    return result 


print(sorted(loneliest('abc d   ef  g   h i j      '))) #, ['g']