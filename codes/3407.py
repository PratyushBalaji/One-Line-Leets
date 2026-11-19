# You are given a string s and a pattern string p, where p contains exactly one '*' character.
# The '*' in p can be replaced with any sequence of zero or more characters.
# Return true if p can be made a substring of s, and false otherwise.

# https://leetcode.com/problems/substring-matching-pattern/

class Solution(object):
    def hasMatch(self, s, p):
        return (lambda pat: (lambda li, ri: False if li == -1 or ri == -1 or li + len(pat[0]) > len(s) - len(pat[1]) - ri else True)(s.find(pat[0]), s[::-1].find(pat[1][::-1])))(p.split('*'))
