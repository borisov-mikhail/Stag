#!/usr/bin/env python3
import cgi
from main_algoritm import get_dividers

form = cgi.FieldStorage()

print("Content-type: text/html")

print("\n<h1>Value: {}</h1>".format(form.getfirst("user_number", 0)))


