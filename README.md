# One Line LeetCode Solutions

I like challenging myself to solve LeetCode problems in one single line. Code Golf : Line Edition

## Rules : 
- Code must be one single line (One expression)

While `x=1; y=2; return x+y` is technically one line, for the spirit of the competition this doesn't count

However, while `return max(list(map(lambda pair: pair[0] ^ pair[1], filter(lambda pair: abs(pair[0]-pair[1]) <= min(pair[0],pair[1]), list(set([(nums[i], nums[j]) for i in range(len(nums)) for j in range(i, len(nums))]))))))` is a mouthful and a half, it is one single expression and so it counts. (btw this is a solution to [Problem #2932](https://leetcode.com/problems/maximum-strong-pair-xor-i/))

All solutions are titled by their corresponding problem number. File contains the problem description, a link to the problem, and the code

Disclaimer : These solutions are usually **extremely** inefficient. Sometimes they shine though.
