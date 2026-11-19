# You are given a 0-indexed array nums that consists of n distinct positive integers.
# Apply m operations to this array, where in the ith operation you replace the number operations[i][0] with operations[i][1].
# It is guaranteed that in the ith operation:
#     operations[i][0] exists in nums.
#     operations[i][1] does not exist in nums.
# Return the array obtained after applying all the operations.

# https://leetcode.com/problems/replace-elements-in-an-array/

class Solution(object):
    def arrayChange(self, nums, operations):
        return (lambda d: sorted(d.keys(), key=d.get))(reduce(lambda d, op: d.update({op[1]: d.pop(op[0])}) or d, operations, {i:x for x,i in enumerate(nums)}))
