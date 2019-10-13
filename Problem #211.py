# Problem 211
#
# Given a string and a pattern, find the starting indices of all occurrences
# of the pattern in the string.
#
# For example, given the string "abracadabra" and the pattern "abr",
# you should return [0, 7].
#
# Solution:

def pattern_finder(str, ptr):
    matches = []
    for i in range(len(str)):
        if len(str) - i >= len(ptr) and str[i:i+len(ptr)] == ptr:
            matches.append(i)
    return matches
