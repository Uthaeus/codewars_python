# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only 


def solve(s):
    upper = 0
    lower = 0
    threshold = len(s) / 2

    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            upper += 1
        elif ord(char) >= 97 and ord(char) <= 122:
            lower += 1

    if lower >= threshold:
        return s.lower()
    elif upper >= threshold:
        return s.upper()



print(solve("code")) #,"code")
print(solve("CODe")) #,"CODE")