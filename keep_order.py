# Task:
# Your job here is to write a function (keepOrder in JS/CoffeeScript, keep_order in Ruby/Crystal/Python, keeporder in Julia), which takes a sorted array ary and a value val, and returns the lowest index where you could insert val to maintain the sorted-ness of the array. The input array will always be sorted in ascending order. It may contain duplicates.


def keep_order(ary, val):
    # your code here
    result = None
    x = 0

    while result == None:
      if ary[x] >= val:
        result = x
      elif x == len(ary) - 1:
        result = x + 1
      x += 1

    return result




print(keep_order([1, 2, 3, 4], 5)) #, 4))
print(keep_order([1, 1, 2, 2, 2], 2)) #, 2))