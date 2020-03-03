# Exercise: Write a Python class to convert an integer to a roman numeral.


class RomanNumerals:

    def __init__(self, int):
        self.num = int

    def int_to_num(self):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        i = 0
        roman_num = ''
        while self.num > i:
            for _ in range(self.num // val[i]):
                roman_num += syb[i]
                self.num -= val[i]
            i += 1
        return roman_num


    def num_to_int(self):


x = RomanNumerals(1248)

print(x.int_to_num())
print(x)