# You are given a string s of even length. 
# Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
# Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.

# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution(object):
    def halvesAreAlike(self, s):
        return (list(map(lambda x: x in set(list('aeiouAEIOU')),s[:len(s)//2]))).count(True) == (list(map(lambda x: x in set(list('aeiouAEIOU')),s[len(s)//2:]))).count(True)