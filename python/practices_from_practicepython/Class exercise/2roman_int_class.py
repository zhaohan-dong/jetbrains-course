#!/usr/bin/python3


class rom_to_int:
    def convert(self, roman_num):
        rom_dict = {"M": 1000, "D": 500,
                    "C": 100, "L": 50, "X": 10,
                    "V": 5, "I": 1}
        num = 0
        for i in range(len(roman_num)):
            if i > 0 and rom_dict[roman_num[i]] > rom_dict[roman_num[i - 1]]:
                num += rom_dict[roman_num[i]] - 2 * rom_dict[roman_num[i - 1]]
            else:
                num += rom_dict[roman_num[i]]
        return num

print(rom_to_int().convert("MMMCMLXXXVI"))