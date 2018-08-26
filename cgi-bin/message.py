#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()


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
    elif user_number == 1 or user_number == 0:
        dividers = user_number
    else:
        dividers = 'ERROR'
    return dividers


print("Content-type: text/html")

value = form.getfirst("user_number", 0)

list_1 = get_dividers(int(value))

print("\n<h1>Dividers: {}</h1>".format(list_1))
