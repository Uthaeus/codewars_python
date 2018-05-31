# You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.

# You should not remove or add elements from/to the array.


def two_sort(array):
    # your code here
    array.sort()
    starred = list(array[0])
    result = '***'.join(starred)

    return result





print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"])) #, 'L***e***t***s'))
print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"])) #, 'c***o***d***e'))