# Return an output string that translates an input string s/$s by replacing each character in s/$s with a number representing the number of times that character occurs in s/$s and separating each number with the character(s) sep/$sep.


def freq_seq(s, sep):
    result = []

    for item in s:
        result.append(str(s.count(item)))

    return sep.join(result) 



print(freq_seq('hello world', '-')) #, '1-1-3-3-2-1-1-2-1-3-1')