# In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.


def solve(s):
    letters = []
    result = ""
    x = -1

    for char in s:
        if char != ' ':
            letters.append(char)

    for char in s:
        if char == ' ':
            result += ' '
        else:
            result += letters[x]
            x -= 1 
    
    return result 
    


print(solve("your code")) #,"edoc ruoy"
print(solve("i love codewars")) #,"s rawe docevoli")