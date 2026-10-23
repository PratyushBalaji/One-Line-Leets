# You are given a 0-indexed integer array nums of size n.
# leftSum[i] is the sum of elements to the left of index i, or 0 if there are none.
# rightSum[i] is the sum of elements to the right of index i, or 0 if there are none.
# Return an integer array answer where answer[i] = |leftSum[i] - rightSum[i]|.

# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        return (lambda leftSum, rightSum: list(map(lambda x: abs(x[0]-x[1]), zip(leftSum,rightSum))))([0] + list(accumulate(nums[:-1])), ([0] + list(accumulate(nums[1:][::-1])))[::-1])
