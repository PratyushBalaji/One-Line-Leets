# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
#     Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

# Beats 100% in runtime!
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return list(accumulate(map(lambda x: 1 if x == 'R' else -1, s))).count(0)