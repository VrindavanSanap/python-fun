#!/usr/bin/python3


from functools import reduce

def product_of_list(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)

numbers = [1, 2, 3, 4, 5]
product = product_of_list(numbers)
print("Product:", product)

