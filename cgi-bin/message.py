#!/usr/bin/env python3

import cgi
import math

form = cgi.FieldStorage()


def get_dividers(number):
    dividers = []
    cur_num = number
    divider = 2
    while cur_num != 1 and divider <= math.ceil(math.sqrt(number)):
        if cur_num % divider == 0:

            dividers.append(divider)

            cur_num /= divider
        else:
            divider += 1
    return sorted(dividers)


print("Content-type: text/html")

value = form.getfirst("user_number", 0)

print("\n<h1>Value: {}</h1>".format(get_dividers(value)))
