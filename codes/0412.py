# Given an integer n, return a string array answer (1-indexed) where:
#     answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#     answer[i] == "Fizz" if i is divisible by 3.
#     answer[i] == "Buzz" if i is divisible by 5.
#     answer[i] == i (as a string) if none of the above conditions are true.

# https://leetcode.com/problems/fizz-buzz/

class Solution(object):
    def fizzBuzz(self, n):
        return list(map(lambda n: (('Fizz' if n%3==0 else '') + ('Buzz' if n%5 == 0 else '') + (str(n) if n%3 != 0 and n%5 != 0 else '')),range(1,n+1)))
    
# Beats 100% in Runtime