# You are given two 2D integer arrays nums1 and nums2.
#     nums1[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.
#     nums2[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.
# Each array contains unique ids and is sorted in ascending order by id.
# Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
#     Only ids that appear in at least one of the two arrays should be included in the resulting array.
#     Each id should be included only once and its value should be the sum of the values of this id in the two arrays. 
#       If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.

# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

class Solution(object):
    def mergeArrays(self, nums1, nums2):
        return (lambda dictionary:[[i,dictionary[i]] for i in sorted(dictionary.keys())])({k: sum(i[1] for i in nums1 + nums2 if i[0] == k) for k, _ in nums1 + nums2})
    
# Super slow because it computes sum everytime in dictionary comprehension.

# Way faster solution : (Beats 100% in runtime)
#```
# ret = {}
# for i in nums1+nums2:
#     ret[i[0]] = ret.get(i[0],0) + i[1]

# return [[i,ret[i]] for i in sorted(ret.keys())]
# ```