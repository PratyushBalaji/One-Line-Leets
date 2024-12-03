# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

# https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution(object):
    def prefixCount(self, words, pref):
        return [i.startswith(pref) for i in words].count(True)
    
# Beats 100% in runtime!