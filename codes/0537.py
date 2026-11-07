# A complex number can be represented as a string on the form "real+imaginaryi" where:
#     real is the real part and is an integer in the range [-100, 100].
#     imaginary is the imaginary part and is an integer in the range [-100, 100].
#     i**2 == -1.
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

# https://leetcode.com/problems/complex-number-multiplication/

# Beats 100% in runtime!
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        return (lambda a,b: "{}+{}i".format(a[0]*b[0]-a[1]*b[1], a[0]*b[1]+b[0]*a[1]))(list(map(int,num1[:-1].split('+'))), list(map(int,num2[:-1].split('+'))))
