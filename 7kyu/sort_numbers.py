# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.


def solution(nums = []):
    nums.sort()
    return nums 


print(solution([1,2,10,5])) #, [1,2,5,10])