# You are given a positive integer x. Your task is to count the number of cells in a table that contain number x.
# sum(x.count('foobar') for x in list)

def count_number(n, x):
    # count = 0

    # Matrix = [[0 for i in range(n)] for j in range(n)]
    # for d1 in range(n):
    #     for d2 in range(n):
    #         Matrix[d1][d2] = (d1 + 1) * (d2 + 1) 

    # return sum(m.count(x) for m in Matrix)

    return sum(1 for i in range(1, n + 1) if x % i == 0 and  x // i <= n)



print(count_number(6,12)) #,4)
print(count_number(100000,1000000000)) #,16)