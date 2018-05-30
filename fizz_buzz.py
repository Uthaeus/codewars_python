# Write a function that takes an integer and returns an array [A, B, C], where A is the number of multiples of 3 (but not 5) below the given integer, B is the number of multiples of 5 (but not 3) below the given integer and C is the number of multiples of 3 and 5 below the given integer.

# For example, solution(20) should return [5, 2, 1]


def solution(number):
  result = []
  c = 0
  b = 0
  a = 0
  temp = range(1, number)
  for x in temp:
    if x % 3 == 0 and x % 5 == 0:
      c += 1
    elif x % 5 == 0:
      b += 1
    elif x % 3 == 0:
      a += 1
  result.extend((a, b, c))
  return result


print(solution(141)) #, [37, 19, 9])
print(solution(30)) #, [8, 4, 1])