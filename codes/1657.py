# Two strings are considered close if you can attain one from the other using the following operations:
#     Operation 1: Swap any two existing characters.
#         For example, abcde -> aecdb
#     Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#         For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution(object):
    def closeStrings(self, word1, word2):
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and set(list(word1)) == set(list(word2))
