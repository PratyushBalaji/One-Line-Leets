# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. 
# You may return the values in any order. 

# https://leetcode.com/problems/two-out-of-three

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        return list(set(nums1).intersection(set(nums2)) | set(nums3).intersection(set(nums2)) | set(nums1).intersection(set(nums3)))