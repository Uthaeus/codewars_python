# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.


def fake_bin(x):
    result = []

    for n in x:
        if int(n) < 5:
            result.append('0')
        else:
            result.append('1')

    return "".join(result)

a = "45385593107843568"

print(fake_bin(a)) # "01011110001100111"