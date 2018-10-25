# Find the mean (average) of a list of numbers in an array.


def find_average(nums):
    if len(nums) < 1:
        return 0
    return float(sum(nums)) / len(nums)



print(find_average([5, 7, 3, 7])) #, 5.5)
print(find_average([])) #, 0)