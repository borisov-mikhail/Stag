#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()


def get_dividers(user_number):
    # Factorization function
    if user_number > 2:
        dividers = ' '
        divider = 2
        while user_number != 1:
            if user_number % divider == 0:
                dividers = dividers + str(divider) + ', '
                user_number /= divider
            else:
                divider += 1
        dividers = dividers[:len(dividers) - 2]
    elif user_number == 1 or user_number == 0:
        dividers = user_number
    else:
        dividers = 'ERROR'
    return dividers


print("Content-type: text/html")
value = form.getfirst("user_number", 0)    # Reading information from the form
list_1 = get_dividers(int(value))

# Output of results
print("\n<h1>Number: {}</h1>".format(value))
print("\n<h1>Dividers: {}</h1>".format(list_1))
