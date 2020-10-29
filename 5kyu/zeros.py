# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.


def move_zeros(array):
    pre = []
    zeros = []

    for i in array:
        if str(i) == '0':
            if i == '0':
                zeros.append('0')
            elif i == 0:
                zeros.append(0)
        elif isinstance(i, float):
            if i % 2 == 0 and int(i) == 0:
                zeros.append(0)
            else:
                pre.append(i)
        else:
            pre.append(i)

    
    return pre + zeros 


#print(move_zeros([1,2,0,1,0,1,0,3,0,1])) #,[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]

print(move_zeros([0.0, 0.1, '0', False, 1, 2, True, 'a', 0]))