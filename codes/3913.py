# You are given a string s consisting of lowercase English characters.
# Rearrange only the vowels in the string so that they appear in non-increasing order of their frequency.
# If multiple vowels have the same frequency, order them by the position of their first occurrence in s.
# Return the modified string.
# Vowels are 'a', 'e', 'i', 'o', and 'u'.
# The frequency of a letter is the number of times it occurs in the string.

# https://leetcode.com/problems/sort-vowels-by-frequency/

# Beats 100% in runtime!
class Solution(object):
    def sortVowels(self, s):
        return "".join((lambda sortedVowels: [next(sortedVowels) if i in 'aeiou' else i for i in s])(iter(sum(([j]*s.count(j) for j in sorted([i for i in set(list(s)) if i in 'aeiou'], key=lambda x: (-s.count(x), s.index(x)))), []))))
