'''     Filename: NumeralConversion1.1.py
        Author: OneForth
        Date Modified: February 19, 2019
        Sources:
            https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-2.php
            https://stackoverflow.com/questions/42875103/integer-to-roman-number

        Description: This program will convert roman numerals to an integer and vise versa
                     and produce an error msg if wrong keys or values are used.
                     This program can also output all possible numerals below 4000. '''


class roman_conversion:
    def roman_to_integer(self, numeral_to_convert):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        converted_value = 0
        for index in range(len(numeral_to_convert)):
            if index > 0 and roman_values[numeral_to_convert[index]] > roman_values[numeral_to_convert[index - 1]]:
                converted_value += roman_values[numeral_to_convert[index]] - \
                                   2 * roman_values[numeral_to_convert[index - 1]]
            else:
                converted_value += roman_values[numeral_to_convert[index]]
        return converted_value

    def integer_to_roman(self, integer_to_convert):
        values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        roman_chars = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        converted_string = ""
        for index in range(len(values)):
            multiplier = int(integer_to_convert / values[index])
            converted_string += roman_chars[index] * multiplier
            integer_to_convert -= values[index] * multiplier
        return converted_string


while True:
    try:
        selection = int(input("Welcome to my Roman Numeral conversion program!\n"
                              "1) Roman Numeral to Integer (Max MMMCMXCIX)\n"
                              "2) Integer to Roman Numeral (Max 3999)\n"
                              "3) Output every possible Roman Numeral \n"
                              "4) Quit : "))

        if selection == 1:
            numeral = input("Please enter a Roman Numeral to convert: ").upper()
            if roman_conversion.roman_to_integer(roman_conversion, numeral) > 3999:
                print("Numeral incorrect, to large!\n")
            else:
                print(roman_conversion.roman_to_integer(roman_conversion, numeral), '\n')

        elif selection == 2:
            integer = int(input("Please enter a Integer to convert: "))
            print(roman_conversion.integer_to_roman(roman_conversion, integer), '\n')
            if integer > 3999:
                print("Integer to large!\n ")

        elif selection == 3:
            for integer_to_convert in range(4000):
                print(roman_conversion.integer_to_roman(roman_conversion, integer_to_convert))
            print()
        else:
            break

    except ValueError:
        print("Incorrect value input!\n")
    except KeyError:
        print("Incorrect numeral characters!\n")
