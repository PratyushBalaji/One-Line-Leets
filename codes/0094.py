# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Beats 100% in runtime!
class Solution:
    def inorderTraversal(self, root):
        return (lambda f: (lambda x: f(lambda *a: x(x)(*a)))(lambda x: f(lambda *a: x(x)(*a))))(lambda traverse: lambda node: [] if not node else traverse(node.left) + [node.val] + traverse(node.right))(root)

# uses a y-combinator with a single expression helper `def traverse(node): return [] if not node else traverse(node.left) + [node.val] + traverse(node.right)`
