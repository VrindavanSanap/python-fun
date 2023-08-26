#!/usr/bin/python3


from functools import reduce

# Step 1: Map - Square the numbers in the input list
def map_function(number):
    return number * number

# Step 2: Reduce - Sum the squared values
def reduce_function(acc, value):
    return acc + value

# Input data
data = [1, 2, 3, 4, 5]

# Map step: Square the numbers
mapped_data = map(map_function, data)
print(mapped_data )

# Reduce step: Sum the squared values
result = reduce(reduce_function, mapped_data)

print("MapReduce Result:", result)

