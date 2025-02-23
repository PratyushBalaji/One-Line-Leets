# A word is considered valid if:
#     It contains a minimum of 3 characters.
#     It contains only digits (0-9), and English letters (uppercase and lowercase).
#     It includes at least one vowel.
#     It includes at least one consonant.
# You are given a string word.
# Return true if word is valid, otherwise, return false.
# Notes:
#     'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
#     A consonant is an English letter that is not a vowel.
# Constraints:
#     1 <= word.length <= 20
#     word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.

# https://leetcode.com/problems/valid-word

class Solution(object):
    def isValid(self, word):
        return not any([i in word for i in '@#$']) and len(word) >= 3 and any([i in word.lower() for i in 'aeiou']) and any([i in word.lower() for i in 'bcdfghjklmnpqrstvwxyz'])