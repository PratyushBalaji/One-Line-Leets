# Given an integer array nums where the elements are sorted in ascending order, convert it to a binary search tree.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution(object):
    def sortedArrayToBST(self, nums):
        return None if not nums else TreeNode(nums[len(nums)>>1],self.sortedArrayToBST(nums[:len(nums)>>1]),self.sortedArrayToBST(nums[(len(nums)>>1)+1:]))