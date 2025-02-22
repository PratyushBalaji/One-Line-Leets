# You are given a string s consisting only of digits. A valid pair is defined as two adjacent digits in s such that:
#     The first digit is not equal to the second.
#     Each digit in the pair appears in s exactly as many times as its numeric value.
# Return the first valid pair found in the string s when traversing from left to right. If no valid pair exists, return an empty string.

# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string

class Solution(object):
    def findValidPair(self, s):
        return (lambda counts: ([s[i]+s[i+1] for i in range(len(s)-1) if s[i] in counts and s[i+1] != s[i] and s[i+1] in counts]+[""])[0])([str(j[0]) for j in [(int(i),s.count(i)) for i in set(list(s))] if j[0] == j[1]])