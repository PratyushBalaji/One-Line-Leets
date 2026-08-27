# You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].
# The number of global inversions is the number of the different pairs (i, j) where:
#    0 <= i < j < n
#    nums[i] > nums[j]
# The number of local inversions is the number of indices i where:
#    0 <= i < n - 1
#    nums[i] > nums[i + 1]
# Return true if the number of global inversions is equal to the number of local inversions.

# https://leetcode.com/problems/global-and-local-inversions/
# Beats 100% with Tail Call Optimisation!
class Solution(object):
    def isIdealPermutation(self, nums, prevmax=-1, prevind=-1, curmax=-1, maxind=-1, i=0, size=0):
        return self.isIdealPermutation(nums, -1, -1, nums[0], 0, 1, len(nums)) if i == 0 else True if i == size else self.isIdealPermutation(nums, curmax, maxind, nums[i], i, i + 1, size) if nums[i] > curmax else False if (i - maxind > 1 or (nums[i] < prevmax and i - prevind > 1)) else self.isIdealPermutation(nums, prevmax, prevind, curmax, maxind, i + 1, size)

# Alternative one-liner (correct, but TLE)
      # return next((False for i in range(len(nums)-1) for j in range(2,len(nums)-i) if nums[i] > nums[i+j]), True)
      
# Without Ternaries
  # def isIdealPermutation(self, nums, prevmax=-1, prevind=-1, curmax=-1, maxind=-1, i=0, size=0):
  #   if i == 0:
  #       return self.isIdealPermutation(nums, -1, -1, nums[0], 0, 1, len(nums))
  #   elif i == size:
  #       return True
  #   else:
  #       if nums[i] > curmax:
  #           return self.isIdealPermutation(nums, curmax, maxind, nums[i], i, i + 1, size)
  #       elif i - maxind > 1 or (nums[i] < prevmax and i - prevind > 1):
  #           return False
  #       else:
  #           return self.isIdealPermutation(nums, prevmax, prevind, curmax, maxind, i + 1, size)

# Original Iterative Code - while loop
  # def isIdealPermutation(self, nums):
  #     prevmax = -1
  #     prevind = -1
  #     curmax = nums[0]
  #     maxind = 0
  #     i = 1
  #     size = len(nums)
  
  #     while i != size:
  #         if nums[i] > curmax:
  #             prevmax = curmax
  #             prevind = maxind
  #             curmax = nums[i]
  #             maxind = i
  #         elif i - maxind > 1 or (nums[i] < prevmax and i - prevind > 1):
  #             return False
  
  #         i += 1
  
  #     return True
