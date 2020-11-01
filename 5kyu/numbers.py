# Create a function that transforms any positive number to a string representing the number in words. The function should work for all numbers between 0 and 999999.
import math 


def number2words(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundreds = ['hundred', 'thousand', 'million']
    text = ''

    


print(number2words(54)) #, "fifty-four"
print (number2words(120000))