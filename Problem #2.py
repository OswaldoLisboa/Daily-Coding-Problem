# Problem 2
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product
# of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

# Solution with division


def multi_div(array_of_numbers):
    new_list = []
    total = 1
    for i in array_of_numbers:
        total *= i
    for i in array_of_numbers:
        new_list.append(int(total/i))
    return new_list

# Solution without division


def multi_nodiv(array_of_numbers):
    new_list = []
    for i in range(len(array_of_numbers)):
        res = 1
        for j in range(len(array_of_numbers)):
            if j != i:
                res *= array_of_numbers[j]
        new_list.append(res)
    return new_list
