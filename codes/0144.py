# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Beats 100% in runtime and memory!
class Solution(object):
    def preorderTraversal(self, root):
        return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# this solution uses direct recursion on the function. check out 0094.py for a true y-combinator approach to inorder traversal
