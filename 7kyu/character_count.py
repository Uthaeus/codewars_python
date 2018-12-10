# Count the number of occurrences of each character and return it as a list of tuples in order of appearance.


def ordered_count(input):
    diction = {}
    result = []
    for x in input:
        if x not in diction:
            diction[x] = input.count(x)

    for key, value in diction.iteritems():
        temp = (key, value)
        result.append(temp)
    return result  



print(ordered_count('abracadabra')) #, [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)])