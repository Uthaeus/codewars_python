# In this Kata, you will be given a string and two indexes (a and b). Your task is to reverse the portion of that string between those two indices inclusive.


def solve(st,a,b):
    head = st[:a]
    body = st[a: b + 1]
    tail = st[b + 1:]
    
    newBody = body[::-1]

    return head + newBody + tail 


print(solve("codingIsFun",2,100)) #,"conuFsIgnid")
print(solve("codewars",1,5)) #,"cawedors")