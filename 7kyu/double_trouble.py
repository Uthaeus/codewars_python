# Given an array of integers (x), and a target (t), you must find out if any two consecutive numbers in the array sum to t. If so, remove the second number.


def trouble(x, t):
    i = 0
    while i < len(x) - 1:
        if x[i] + x[i + 1] == t:
            del x[i + 1]
            trouble(x, t)
        i += 1
    return x 



#print(trouble([1, 3, 5, 6, 7, 4, 3],7)) #, [1, 3, 5, 6, 7, 4])
print(trouble([4, 1, 1, 1, 4],2)) #, [4, 1, 4]))