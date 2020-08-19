


def accum(s):
    result = []
    ind = 0

    for x in s:
        temp = x.upper()
        temp += x.lower() * ind 
        ind += 1
        result.append(temp)

    return "-".join(result)


print(accum("ZpglnRxqenU")) #, "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")