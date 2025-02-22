# You are given a string s consisting of lowercase English letters. 
# Your task is to find the maximum difference between the frequency of two characters in the string such that:
#     One of the characters has an even frequency in the string.
#     The other character has an odd frequency in the string.
# Return the maximum difference, calculated as the frequency of the character with an odd frequency minus the frequency of the character with an even frequency.

# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i

class Solution(object):
    def maxDifference(self, s):
        return max(map(lambda x:max([s.count(i) for i in set(list(s)) if s.count(i) % 2 == 1]) - x, [s.count(i) for i in set(list(s)) if s.count(i) % 2 == 0]))