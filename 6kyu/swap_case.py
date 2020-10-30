# Your job is to change the given string s using a non-negative integer n


def swap(s,n):
    b = bin(n)[2:]
    bin_text = b 
    bin_count = 0
    x = 0
    text = ""

    while x < len(s):
        if bin_count >= len(bin_text):
            bin_text += b 
        if ord(s[x]) >= 65 and ord(s[x]) <= 90:
            if bin_text[bin_count] == '1':
                text += s[x].lower()
            else:
                text += s[x]
            bin_count += 1
        elif ord(s[x]) >= 97 and ord(s[x]) <= 122:
            if bin_text[bin_count] == '1':
                text += s[x].upper()
            else:
                text += s[x]
            bin_count += 1
        else:
            text += s[x]
        x += 1

    return text 


print(swap('Hello world!', 11)) #, 'heLLO wORLd!'