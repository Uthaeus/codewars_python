# You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number n the kth bit from the right was initially set to 0, but its current value might be different. It's now up to you to write a function that will change the kth bit of n back to 0.


def kill_kth_bit(n, k):
    temp = list(bin(n)[2:])
    b = k * -1
    while len(temp) <= k:
        temp = ['0'] + temp 
    temp[b] = '0'
    return int(''.join(temp), 2) 



print(kill_kth_bit(37,4)) # , 37)
print(kill_kth_bit(0,4)) # , 0)