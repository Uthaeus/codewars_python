# Complete the function so that it finds the mean of the three scores passed to it and returns the letter value associated with that grade


def get_grade(s1, s2, s3):
    result = (s1 + s2 + s3) / 3
    if result >= 90:
        return 'A'
    elif result >= 80 and result < 90:
        return 'B'
    elif result >= 70 and result < 80:
        return 'C'
    elif result >= 60 and result < 70:
        return 'D'
    elif result < 60:
        return 'F'



print(get_grade(100, 85, 96)) #, "A", "get_grade(100, 85, 96)")