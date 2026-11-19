# You are given an integer array target and an integer n.
# You have an empty stack with the two following operations:
#     "Push": pushes an integer to the top of the stack.
#     "Pop": removes the integer on the top of the stack.
# You also have a stream of the integers in the range [1, n].
# Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target.
# You should follow the following rules:
#     If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
#     If the stack is not empty, pop the integer at the top of the stack.
#     If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
# Return the stack operations needed to build target following the mentioned rules.
# If there are multiple valid answers, return any of them.

# https://leetcode.com/problems/build-an-array-with-stack-operations/

# Beats 100% in runtime and is a lot more memory efficient
class Solution(object):
    def buildArray(self, target, n):
        return reduce(lambda x,y: (x[0] + ["Push","Pop"]*(y-x[1]-1) + ["Push"], y), target, ([],0))[0]

# Original solution: Beats 100% in runtime!
# return reduce(lambda x,y: (x[0] + ["Push"], x[1]+1) if target[x[1]] == y else (x[0] + ["Push","Pop"], x[1]), range(1, target[-1]+1),([],0))[0]
