# You have intercepted a secret message encoded as a string of numbers.
# The message is decoded via the following mapping:
# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'
# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").
# For example, "11106" can be decoded into:
#     "AAJF" with the grouping (1, 1, 10, 6)
#     "KJF" with the grouping (11, 10, 6)
#     The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.
# Given a string s containing only digits, return the number of ways to decode it.
# If the entire string cannot be decoded in any valid way, return 0.
# The test cases are generated so that the answer fits in a 32-bit integer.

# https://leetcode.com/problems/decode-ways/

# Beats 100% in runtime and memory!
class Solution(object):
    def numDecodings(self, s):
        return sum(reduce(lambda x, n: (lambda t: [(t if n == 1 else 0), (t if n == 2 else 0), (t if 3 <= n <= 9 else 0) + x[0] + (x[1] if 0 <= n <= 6 else 0)])(sum(x)), map(int, list(s)), [0,0,1]))
