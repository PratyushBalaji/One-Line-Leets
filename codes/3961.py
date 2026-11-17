# You are given a 2D integer array units of size m × n where units[i][j] represents the capacity of the jth unit in the ith device.
# Each device contains exactly n units.
# The rating of a device is the minimum capacity among all its units.
# You may perform the following operation any number of times (including zero):
#     Choose a device i that has not been used as a source before.
#     Remove exactly one unit from device i and add it to any different device.
#     Then mark device i as used, so it cannot be chosen again as a source.
# Return the maximum possible sum of the ratings of all devices after any number of such operations.
# Note:
#     Devices can receive units from multiple devices, regardless of whether they have been selected.
#     The rating of an empty device is 0.

# https://leetcode.com/problems/maximize-sum-of-device-ratings/

class Solution(object):
    def maxRatings(self, units):
        return sum(i[0] for i in units) if len(units[0]) == 1 else (lambda nU: sum(i[1] for i in nU) - min(nU, key=lambda r: r[1])[1] + min(min(i) for i in nU))([sorted(i)[:2] for i in units])
