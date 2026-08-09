# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# https://leetcode.com/problems/same-tree/description/

# Beats 100% in runtime!
class Solution:
    def isSameTree(self, p, q):
        return True if not p and not q else False if not p or not q else p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
