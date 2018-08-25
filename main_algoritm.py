import math

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

print(get_dividers(51))
