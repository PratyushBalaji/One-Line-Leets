# Given an array of integers arr.
# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
# Let's define a and b as follows:
#     a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
#     b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.
# Return the number of triplets (i, j and k) Where a == b.

# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

class Solution(object):
    def countTriplets(self, arr):
        return (lambda pref: sum(j-i for i in range(len(pref)-2) for j in range(i+1, len(pref)-1) if pref[i] == pref[j+1]))(reduce(lambda p, x: (p.append(p[-1] ^ x), p)[1], arr, [0]))
