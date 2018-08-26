import math


def get_dividers(user_number):
    if user_number > 2:
        dividers = ' '
        divider = 2
        while user_number != 1:
            if user_number % divider == 0:
                dividers = dividers + str(divider) + ' '
                user_number /= divider
            else:
                divider += 1
    else:
        dividers = 'ERROR'
    return dividers


print(get_dividers(1.25))
print(get_dividers(51.0))
print(get_dividers(51.65))
print(get_dividers(1001))
print(get_dividers(66))
