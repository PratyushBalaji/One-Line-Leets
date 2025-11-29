# You are given a 0-indexed integer array nums. 
# An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. 
# Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. 
# Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].
# Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.
# Return the number of hills and valleys in nums.

# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

# Beats 100% in runtime and memory!
class Solution(object):
    def countHillValley(self, nums):
        return (lambda newnums: sum([1 for i in range(1,len(newnums)-1) if (newnums[i-1] > newnums[i] and newnums[i] < newnums[i+1]) or (newnums[i-1] < newnums[i] and newnums[i] > newnums[i+1])]))([nums[i] for i in range(len(nums)) if (i==0 or nums[i] != nums[i-1])])