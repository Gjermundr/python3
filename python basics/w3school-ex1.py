# Exercise: Write a Python class to convert an integer to a roman numeral.


class RomanNumerals:
    def int_to_num(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i = 0
        roman_num = ''
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


    def num_to_int(self, num):
        roman_num = num.split()
        syb_val = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        i = 0
        print(roman_num)
        #for _ in roman_val:


x = RomanNumerals()
print(x.int_to_num(9345))
print(x.num_to_int('MDLX'))
help(str.split)
