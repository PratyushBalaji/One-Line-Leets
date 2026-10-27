# You are given a 1-indexed array of distinct integers nums of length n.
# Append the first element to arr1 and the second element to arr2.
# For each remaining element, append it to arr1 if its last element is greater
# than the last element of arr2; otherwise, append it to arr2.
# Return the concatenation of arr1 and arr2.

# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

# Python 2: uses reduce() and tuple unpacking in a lambda.
class Solution(object):
    def resultArray(self, nums):
        return (lambda x : x[2]+x[3])(reduce(lambda (la1, la2, a1, a2),y : (y, la2, a1+[y], a2) if la1 > la2 else (la1, y, a1, a2+[y]), nums[2:], (nums[0],nums[1],[nums[0]],[nums[1]])))
