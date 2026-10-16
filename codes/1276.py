# Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:
#     Jumbo Burger: 4 tomato slices and 1 cheese slice.
#     Small Burger: 2 Tomato slices and 1 cheese slice.
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. 
# If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        return (lambda j,s: [] if (tomatoSlices%2 == 1 or j < 0 or s < 0) else [j,s])(tomatoSlices/2 - cheeseSlices, 2*cheeseSlices - tomatoSlices/2)
