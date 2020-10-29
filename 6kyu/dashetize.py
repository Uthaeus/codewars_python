# Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.


def dashatize(num):
    result = ''
    n = str(num)
    count = 0
    for l in n:
        isodd = int(l) % 2 != 0

        if isodd and count < len(n) - 1:
            if len(result) > 1 and result[-1] != '-':
                result += '-'
            result += l + '-'
        elif isodd:
            if result [-1] != '-':
                result += '-'
            result += l 
        count += 1

    return result 


print(dashatize(5311)) #,"5-3-1-1"