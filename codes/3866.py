# You are given an integer array nums.
# Return an integer denoting the first even integer (earliest by array index) that appears exactly once in nums. 
# If no such integer exists, return -1.
# An integer x is considered even if it is divisible by 2.

# https://leetcode.com/problems/first-unique-even-element/

# combined cnt[i]==1 and i%2==0 in one condition. this works because cnt[i] >= 1 and i%2 in {0,1}
class Solution(object):
    def firstUniqueEven(self, nums):
        return (lambda cnt: next((i for i in nums if cnt[i]+(i%2)==1),-1))(Counter(nums))
