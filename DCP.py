# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
from itertools import combinations

def return_sum_value(input_list, sum_value) -> bool:
    for var in combinations(input_list, 2):
        if var[0] + var[1] == sum_value:
            return True
        else:
            continue
    return False

input_list = [10, 15, 3, 7]
assert return_sum_value(input_list, 10)
input_list = [1, 5, 5, 10, 15, 3, 7]
assert return_sum_value(input_list, 10)

# Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

from functools import reduce

def return_multiplied_array(input_list) -> list:
    product = reduce(lambda x, y : x*y, input_list)
    return [product/each for each in input_list]

def return_multiplied_array_v2(input_list0) -> list:


input_list = [1, 2, 3, 4, 5]
assert return_multiplied_array(input_list) == [120, 60, 40, 30, 24]
assert return_multiplied_array(input_list) == return_multiplied_array_v2(input_list)
input_list = [3, 2, 1]
assert return_multiplied_array(input_list) == [2, 3, 6]
assert return_multiplied_array(input_list) == return_multiplied_array_v2(input_list)
    
