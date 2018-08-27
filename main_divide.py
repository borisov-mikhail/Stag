def get_dividers(user_number):
    if user_number > 2:
        dividers = ' '
        divider = 2
        while user_number != 1:
            if user_number % divider == 0:
                dividers = dividers + str(divider) + ', '
                user_number /= divider
            else:
                divider += 1
    else:
        dividers = 'ERROR'
    return dividers[:len(dividers)-2]


a = get_dividers(1000)
print(a[:len(a)-2])
print(get_dividers(125))
print(get_dividers(-15))
print(get_dividers(51))
print(get_dividers(1001))
print(get_dividers(66))
