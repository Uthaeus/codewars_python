# You will be given the first row of the triangle as a string and its your job to return the final colour which would appear in the bottom row as a string. In the case of the example above, you would the given RRGBRGBB you should return G.


def triangle(row):
    diction = {
        'GG': "G",
        'BG': 'R',
        'RG': 'B',
        'BR': 'G',
        'RB': 'G',
        'GR': 'B',
        'GB': 'R',
        'RR': 'R',
        'BB': 'B'
    }
    while len(row) > 1:
        temp = ''
        x = 0
        while x < len(row) - 1:
            temp += diction[row[x:x+2]]
            x += 1
        row = temp 
    return row 




print(triangle('RBRGBRBGGRRRBGBBBGG')) #, 'G')
print(triangle('RBRGBRB')) #, 'G')
print(triangle('B')) #, 'B')