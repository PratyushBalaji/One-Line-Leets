# You are given a 0-indexed array of string words and two integers left and right.
# A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.
# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution(object):
    def vowelStrings(self, words, left, right):
        return sum(1 for x in words[left:right+1] if x[0] in 'aeiou' and x[-1] in 'aeiou')
