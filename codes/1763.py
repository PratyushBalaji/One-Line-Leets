# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. 
# For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. 
# If there are none, return an empty string.

# https://leetcode.com/problems/longest-nice-substring/

class Solution(object):
    def longestNiceSubstring(self, s):
        return next((s[j:j+i] for i in range(len(s),1,-1) for j in range(len(s)-i+1) if (lambda x: all([i in x and i.upper() in x for i in list(x.lower())]))(s[j:j+i])),'')