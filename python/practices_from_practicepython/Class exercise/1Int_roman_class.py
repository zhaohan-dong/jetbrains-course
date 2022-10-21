#!/usr/bin/python3


# https://www.w3resource.com/python-exercises/class-exercises/index.php

class int_roman:
    def int_to_roman(self, num):
        val = [1000, 900, 500, 400,
               100, 90, 50, 40, 10,
               9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV", "I"]
        roman_num = ""
        i = 0
        while num > 0:
            for j in range (num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(int_roman().int_to_roman(1200))
