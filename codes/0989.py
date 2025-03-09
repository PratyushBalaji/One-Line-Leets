# The array-form of an integer num is an array representing its digits in left to right order.
#     For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

# https://leetcode.com/problems/add-to-array-form-of-integer

class Solution(object):
    def addToArrayForm(self, num, k):
        return map(int,list(str(k+int("".join(map(str,num))))))