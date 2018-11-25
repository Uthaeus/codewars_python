# For this first Kata, you will write a function hamming_distance(a, b) with two equal-length strings containing only 0s and 1s as parameters. There is no need to test the parameters for validity (but you can, if you want).The function's output should be the hamming distance of the two strings as an integer


def hamming_distance(a, b):
    count = 0
    x = 0
    while x < len(a):
        if a[x] != b[x]:
            count += 1
        x += 1
    return count 



print(hamming_distance('1010', '0101')) #, 4)
print(hamming_distance('100101011011010010010', '101100010110010110101')) #, 9)