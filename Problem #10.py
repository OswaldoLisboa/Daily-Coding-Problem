# Problem 10
#
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
#
# Solution:

import time


def scheduler(f, n):
    time.sleep(n/1000)
    return f
