# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
# Return the minimum number of operations to make all elements of nums divisible by 3.

# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

# Beats 100% in runtime!
class Solution(object):
    def minimumOperations(self, nums):
        return len([i for i in nums if i%3 != 0])