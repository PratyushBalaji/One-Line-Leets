# You are given a 0-indexed integer array nums representing the score of students in an exam. 
# The teacher would like to form one non-empty group of students with maximal strength, 
# where the strength of a group of students of indices i_0, i_1, i_2, ... , i_k is defined as nums[i_0] * nums[i_1] * nums[i_2] * ... * nums[i_k​].

# Return the maximum strength of a group the teacher can create.

# https://leetcode.com/problems/maximum-strength-of-a-group/

class Solution(object):
    def maxStrength(self, nums):
        return (lambda neg,pos: max(nums) if len(neg) <= 1 and len(pos) <= 1 else reduce(lambda x,y:x*y, pos + [neg[i-1]*neg[i] for i in range(1,len(neg),2)], 1))(sorted([i for i in nums if i < 0]),[i for i in nums if i > 0])