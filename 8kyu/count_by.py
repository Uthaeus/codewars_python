# Create a function with two arguments that will return a list of length (n) with multiples of (x).


def count_by(x, n):
    i = 1
    result = []

    while i <= n:
        result.append(x * i)
        i += 1

    return result 



print(list(count_by(50, 5))) #, [50, 100, 150, 200, 250])