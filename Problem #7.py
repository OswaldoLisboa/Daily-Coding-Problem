# Problem 7
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
# count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

# Solution


def decode_possibilities(message):
    
    if len(message) == 1:
        return 1
    elif len(message) == 2:
        if int(message[0]) == 1 or (int(message[0]) == 2 and int(message[1]) <= 6):
            return 2
        else:
            return 1
    else:
        if int(message[0]) == 1 or (int(message[0]) == 2 and int(message[1]) <= 6):
            return decode_possibilities(message[2:]) + decode_possibilities(message[1:])
        else:
            return  decode_possibilities(message[1:])
