import math


def get_dividers(user_number):
    dividers = []
    divider = 2
    while user_number != 1:
        if user_number % divider == 0:
            dividers.append(divider)
            user_number /= divider
        else:
            divider += 1
    return dividers


print(get_dividers(125))
print(get_dividers(51))
print(get_dividers(5165))
print(get_dividers(1001))
print(get_dividers(66))
