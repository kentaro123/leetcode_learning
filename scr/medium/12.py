import numpy as np
def intToRoman(num):
    r = 'M' * (num // 1000)
    r += 'C' * (num % 1000 // 100)
    r += 'X' * (num % 100 // 10)
    r += 'I' * (num % 10 // 1)
    r = r.replace('C' * 9, 'CM')
    r = r.replace('C' * 5, 'D')
    r = r.replace('C' * 4, 'CD')
    r = r.replace('X' * 9, 'XC')
    r = r.replace('X' * 5, 'L')
    r = r.replace('X' * 4, 'XL')
    r = r.replace('I' * 9, 'IX')
    r = r.replace('I' * 5, 'V')
    r = r.replace('I' * 4, 'IV')
    return r

print(intToRoman(1994))
