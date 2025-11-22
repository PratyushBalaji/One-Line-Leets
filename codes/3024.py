# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.
#     A triangle is called equilateral if it has all sides of equal length.
#     A triangle is called isosceles if it has exactly two sides of equal length.
#     A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

# https://leetcode.com/problems/type-of-triangle/

# Beats 100% in runtime!
class Solution(object):
    def triangleType(self, nums):
        return "none" if sum(nums) - 2*max(nums) <= 0 else "scalene" if len(set(nums)) == 3 else "isosceles" if len(set(nums)) == 2 else "equilateral"