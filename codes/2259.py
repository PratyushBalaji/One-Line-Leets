# You are given a string number representing a positive integer and a character digit.
# Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. 
# The test cases are generated such that digit occurs at least once in number.

# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution(object):
    def removeDigit(self, number, digit):
        return str(max([int(number[:i]+number[i+1:]) for i in range(len(number)) if number[i]==digit]))