# Alice and Bob are playing a game. Initially, Alice has a string word = "a".
# You are given a positive integer k.
# Now Bob will ask Alice to perform the following operation forever:
#     Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
# For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
# Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution:
    def kthCharacter(self, k: int) -> str:        
        return (lambda its: (lambda inc: (lambda ret: [ret for i in range(its) if (ret:=inc(ret))][-1][k-1])('a'))(lambda s: s + "".join([('a' if i == 'z' else chr(ord(i)+1)) for i in s])))(next((i for i in range(1,k+1) if 1<<i >= k)))