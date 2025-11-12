# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution(object):
    def maxDepth(self, root):
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right)) if root else 0