# Task
# Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .


def max_tri_sum(numbers):
    #your code here
  result = []
  total = 0
  nums = sorted(numbers)
  nums.reverse()
 
  for x in nums:
    if x not in result:     
      result.append(x)

  temp = result[0:3]
  for x in temp:
    total += x

  return total



print(max_tri_sum([-13,-50,57,13,67,-13,57,108,67]))  #,232))