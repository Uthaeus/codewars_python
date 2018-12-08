# Given an array, return the difference between the count of even numbers and the count of odd numbers. 0 will be considered an even number.


def solve(a):
    nums = [n for n in a if type(n) == int]
    e = list(filter(lambda x: x % 2 == 0, nums))
    o = list(filter(lambda x: x % 2 != 0, nums))
    return len(e) - len(o)



print(solve([13, 6, 8, 15, 4, 8, 13])) #,1)
print(solve([1,'a', 17, 8,'e', 3,'i', 12, 1])) #,-2)