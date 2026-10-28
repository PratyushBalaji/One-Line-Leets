# There are n ice cream bars, where costs[i] is the price of the ith bar in coins.
# The boy initially has coins coins to spend and can buy the bars in any order.
# Return the maximum number of ice cream bars he can buy.
# You must solve the problem by counting sort.

# https://leetcode.com/problems/maximum-ice-cream-bars/

# Python 2: uses reduce() and tuple unpacking in a lambda.
class Solution(object):
    def maxIceCream(self, costs, coins):
        return reduce(lambda (price, bars), i: (price + i, bars + 1) if price + i <= coins else (price, bars), sorted(costs), (0,0))[1]

        # costs.sort()
        # price = 0
        # bars = 0
        # for i in costs:
        #     if price + i <= coins:
        #         price += i
        #         bars += 1
        #     else:
        #         return bars

        # return bars

# This version beats 60% runtime and 100% memory!
