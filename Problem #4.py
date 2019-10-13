# Problem 4
#
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.


def lowest_positive(array):
    for i in range(0, len(array)):
        if array[i] < 0:
            array[i] = 0
    lowest = min(array)
    while True:
        lowest += 1
        if lowest not in array:
            return lowest
