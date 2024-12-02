# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.

# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution(object):
    def countGoodSubstrings(self, s):
        return 0 if len(s)<3 else sum([1 for i in range(len(list(s))) if len(set(s[i:i+3]))==3])