# You are given two strings s1 and s2 of equal length. 
# A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        return (lambda ret: False if (len(s1) != len(s2)) or (len(ret) not in {0,2}) else len(ret) == 0 or (s1[ret[0]] == s2[ret[1]] and s1[ret[1]] == s2[ret[0]]))((lambda x, y: [i for i in range(len(x)) if x[i] != y[i]])(s1, s2))
    
# Beats 100% in Runtime