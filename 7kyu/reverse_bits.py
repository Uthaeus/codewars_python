# Write a function that reverses the bits in an integer.


def reverse_bits(n):
    temp = bin(n)[2:]
    rev = ''
    ind = len(temp)
    while ind > 0:
        rev += temp[ind - 1]
        ind -= 1
    return int(rev, 2)



print(reverse_bits(2017)) #, 1087)