# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Beats 100% in runtime and memory!
class Solution(object):
    def postorderTraversal(self, root):
        return [] if not root else [root.val] + self.postorderTraversal(root.left) + self.postorderTraversal(root.right)

# this solution uses direct recursion on the function. check out 0094.py for a true y-combinator approach to inorder traversal
