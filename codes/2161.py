# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
#     Every element less than pivot appears before every element greater than pivot.
#     Every element equal to pivot appears in between the elements less than and greater than pivot.
#     The relative order of the elements less than pivot and the elements greater than pivot is maintained.
#         More formally, consider every p_i, p_j where p_i is the new position of the ith element and p_j is the new position of the jth element. 
#         If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
# Return nums after the rearrangement.

# https://leetcode.com/problems/partition-array-according-to-given-pivot

class Solution(object):
    def pivotArray(self, nums, pivot):
        return list(filter(lambda x: x<pivot,nums)) + ([pivot]*nums.count(pivot)) + list(filter(lambda x: x>pivot,nums))