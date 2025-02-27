# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
# Return true if the square is white, and false if the square is black.
# The coordinate will always represent a valid chessboard square. 
# The coordinate will always have the letter first, and the number second

# https://leetcode.com/problems/determine-color-of-a-chessboard-square

class Solution(object):
    def squareIsWhite(self, coordinates):
        return ((ord(coordinates[0])-96) + int(coordinates[1])) % 2 == 1
    
# Beats 100% in runtime!