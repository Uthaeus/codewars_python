# Task
# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ().


def expression_matter(a, b, c):
  highest = 0
  cases = []

  p1 = (a + b) * c 
  p2 = a + (b * c)
  p3 = a + b + c 
  p4 = a + b * c 
  p5 = a * b + c 
  p6 = a * b * c
  p7 = a * (b + c) 
  cases.extend((p1, p2, p3, p4, p5, p6, p7))

  for x in cases:
    if x > highest:
      highest = x

  return highest



print(expression_matter(3, 5, 7))  #, 105
print(expression_matter(5, 1, 3)) #, 20)