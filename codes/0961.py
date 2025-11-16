# You are given an integer array nums with the following properties:
#     nums.length == 2 * n.
#     nums contains n + 1 unique elements.
#     Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

# Beats 100% in runtime!
class Solution(object):
    def repeatedNTimes(self, nums):
        return (lambda seen: next(i for i in nums if i in seen or seen.add(i)))(set())