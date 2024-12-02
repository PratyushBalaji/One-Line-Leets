# Given an array of strings words, return the first palindromic string in the array. 
# If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution(object):
    def firstPalindrome(self, words):
        return ([i for i in words if i == i[::-1]]+[""])[0]