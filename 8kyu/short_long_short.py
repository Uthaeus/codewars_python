# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( length 0 ).


def solution(a, b):
    if len(a) > len(b):
        longer = a 
        shorter = b 
    else:
        longer = b 
        shorter = a 

    return shorter + longer + shorter 


print(solution('45', '1')) # '1451'