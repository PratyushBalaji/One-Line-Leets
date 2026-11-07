# You are given a string s and an integer t. In each transformation, replace
# 'z' with "ab" and every other letter with the next letter in the alphabet.
# Return the length after t transformations, modulo 10^9 + 7.

# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

# Beats 94.12% in runtime!
class Solution(object):
    def lengthAfterTransformations(self, s, t):
        return sum(reduce(lambda c, _: [c[-1], (c[0]+c[-1]) % (10**9+7)] + c[1:-1], range(t), [s.count(chr(i+97)) for i in range(26)])) % (10**9+7)
