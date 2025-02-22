# You are given a string num consisting of only digits. 
# A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.
# Return true if num is balanced, otherwise return false.

# https://leetcode.com/problems/check-balanced-string

class Solution(object):
    def isBalanced(self, num):
        return sum([int(num[i]) if i%2 == 0 else -int(num[i]) for i in range(len(num))]) == 0