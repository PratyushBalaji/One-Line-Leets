# Given two strings a and b, return the length of the longest uncommon subsequence between a and b.
# If no such uncommon subsequence exists, return -1.
# An uncommon subsequence between two strings is a string that is a subsequence of exactly one of them.

# https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution(object):
    def findLUSlength(self, a, b):
        return -1 if a == b else max(len(a),len(b))
