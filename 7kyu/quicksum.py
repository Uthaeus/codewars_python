


def quicksum(packet):
    p = list(packet)
    alph = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    check = 0
    
    for index, val in enumerate(p, start=1):
        if val not in alph:
            return 0
        check += (alph.find(val) * index)

    return check 



print(quicksum("MID CENTRAL")) #, 650)
print(quicksum("234 234 WEF ASDF AAA 554211 ???? ")) #, 0)