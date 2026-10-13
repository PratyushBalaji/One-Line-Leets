# You are given two non-negative integers n and s.
# Return the largest integer that has at most n digits and whose sum of digits is s. If no such integer exists, return -1.

# https://leetcode.com/problems/largest-integer-with-given-digit-sum/description/

# Beats 100% in runtime and memory!
class Solution(object):
    def largestInteger(self, n, s):
        return -1 if s > 9*n else int(''.join(map(str, [(9 if s-(9*i) > 9 else max(0,s-(9*i))) for i in range(n)])))
