# Move every letter in the provided string forward 10 letters through the alphabet.


def move_ten(st):
    result = ''
    for letter in st:
        if ord(letter) + 10 > 122:
            result += chr((ord(letter) + 10) - 26)
        else:
            result += chr(ord(letter) + 10)
    return result 



print(move_ten("exampletesthere")) #, "ohkwzvodocdrobo")