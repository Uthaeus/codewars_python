# write a function inverse_slice() that takes three arguments: a list items, an integer a and an integer b. The function should return a new list with the slice specified by items[a:b] excluded. For example:


def inverse_slice(items, a, b):
    result = items[0:a] + items[b:]
    return result 



# print(inverse_slice([12, 14, 63, 72, 55, 24], 0, 3)) #, [72, 55, 24])
print(inverse_slice(['Intuition', 'is', 'a', 'poor', 'guide', 'when', 'facing', 'probabilistic', 'evidence'], 5, 13))
#, ['Intuition', 'is', 'a', 'poor', 'guide'])