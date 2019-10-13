# Problem 11
#
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
#
# Solution:


def autocomplete(s, query_strings):
    strings = []
    for i in query_strings:
        if i[:len(s)] == s:
            strings.append(i)
    return strings
