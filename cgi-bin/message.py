#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()


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


print("Content-type: text/html")

value = form.getfirst("user_number", 0)

list_1 = get_dividers(value)

print("\n<h1>Dividers: {}</h1>".format(list_1[1]))
