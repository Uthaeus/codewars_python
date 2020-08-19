# Count the number of occurrences of each character and return it as a list of tuples in order of appearance.


def ordered_count(input):
    check = ''
    result = []
    for x in input:
        if x not in check:
            temp = (x, input.count(x))
            result.append(temp)
            check += x
    return result 



print(ordered_count('abracadabra')) #, [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)])