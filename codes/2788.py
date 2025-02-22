# Given an array of strings words and a character separator, split each string in words by separator.
# Return an array of strings containing the new strings formed after the splits, excluding empty strings.
# Notes
#     separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
#     A split may result in more than two strings.
#     The resulting strings must maintain the same order as they were initially given.


# https://leetcode.com/problems/split-strings-by-separator

class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        return filter(lambda x:x!='',reduce(lambda x,y:x+y.split(separator),words,[]))