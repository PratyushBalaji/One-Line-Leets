# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). 
# If the character ch does not exist in word, do nothing.
#     For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). 
#     The resulting string will be "dcbaefd".
# Return the resulting string.

# https://leetcode.com/problems/reverse-prefix-of-word

class Solution(object):
    def reversePrefix(self, word, ch):
        return word if ch not in word else (lambda i:word[:i+1][::-1] + word[i+1:])(word.index(ch))