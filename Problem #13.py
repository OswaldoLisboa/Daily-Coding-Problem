# Problem 13
#
# Given an integer k and a string s, find the length of the longest substring
# that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k
# distinct characters is "bcb".None
#
# Solution:


def unique_chars(s):
    uq_chars = set()
    for i in s:
        uq_chars.add(i)
    return len(uq_chars)


def longest_substing(k, s):
    longest = 0
    for i in range(len(s)):
        j = 1
        while j <= len(s[i:]):
            if unique_chars(s[i:i+j]) <= k and len(s[i:i+j]) > longest:
                longest = len(s[i:i+j])
            j += 1
    return longest
