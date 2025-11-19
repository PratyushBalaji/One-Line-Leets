# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
# A binary search tree is a binary tree where for every node, 
#   any descendant of Node.left has a value strictly less than Node.val, and
#   any descendant of Node.right has a value strictly greater than Node.val.
# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Beats 100% in runtime!

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        return None if not preorder else TreeNode(val=preorder[0], left=self.bstFromPreorder([i for i in preorder if i < preorder[0]]), right=self.bstFromPreorder([i for i in preorder if i > preorder[0]]))