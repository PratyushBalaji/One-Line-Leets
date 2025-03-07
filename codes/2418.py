# You are given an array of strings names, and an array heights that consists of distinct positive integers. 
# Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.

# https://leetcode.com/problems/sort-the-people

class Solution(object):
    def sortPeople(self, names, heights):
        return [i[1] for i in sorted([[heights[j],names[j]] for j in range(len(names))],reverse=True)]