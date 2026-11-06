# Showcase

Below is a list of a few solutions that I want to showcase, such as the longest, shortest, and some otherwise interesting solutions

## Longest and Shortest Solutions :
Metric : Convert all variable (and parameter) names to single characters, remove as much whitespace as possible, measure number of characters in the return statement (including the word `return`)

Yes, the code logic itself could be made longer (or *shorter?*) to artificially modify the result, but I'll try not to intentionally write extremely long code :P

### Shortest Solution : 
[#1025](https://leetcode.com/problems/divisor-game/) `divisorGame(self, n)` : 12 Characters

`return n%2<1`

### Longest Solution : 
[#2732](https://leetcode.com/problems/find-a-good-subset-of-the-matrix/) `goodSubsetofBinaryMatrix(self, g)` : 232 Characters

`return(lambda d:(lambda v,k,l:next((sorted([v[i],v[j]])for i in range(l-1)for j in range(i+1,l)if k[i]&k[j]==0),[0]if k[0]==0 else[]))(d.values(),d.keys(),len(d)))({sum(i<<x for x,i in enumerate(j[::-1])):y for y,j in enumerate(g)})`

Beats 100% in memory!

---

## Solutions I find interesting :

### Problem [#0319](https://leetcode.com/problems/bulb-switcher/) - Bulb Switcher

`return int(n**0.5)`

This is the same problem as the [100 Monkeys Problem](https://github.com/PratyushBalaji/100-Monkeys), which I explored in another repository—just with bulbs instead of doors!

Each bulb is toggled once for every factor of its number. Factors come in pairs, so most bulbs end up off again. Only doors toggled an odd number of times (i.e. an odd number of factors) stay on, and for perfect squares like 1, 4, or 9, their square root is paired with itself, thus only contributes one toggle and leaves the bulb on!

Since this problem only asks how many bulbs remain on, we don't need to simulate anything or even list the squares. There are exactly `floor(sqrt(n))` perfect squares up to `n`, giving us this tiny one-liner. My 100-Monkeys repo walks through the reasoning and several approaches to finding those squares through continuous optimisation as the pattern reveals itself.

### Problem [#2248](https://leetcode.com/problems/intersection-of-multiple-arrays) - Intersection of Multiple Arrays
`return sorted(reduce(lambda x,y:[i for i in x if i in y],nums))`

Uses `reduce()` which works like `foldr`, accumulating results and iterating through nums to find the intersection. First solution where I tried to incorporate my (then) newly gained knowledge of the "fold" Abstract List Functions.

### Problem [#1790](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal) - Check if One String Swap Can Make Strings Equal
`return (lambda ret: False if (len(s1) != len(s2)) or (len(ret) not in {0,2}) else len(ret) == 0 or (s1[ret[0]] == s2[ret[1]] and s1[ret[1]] == s2[ret[0]]))((lambda x, y: [i for i in range(len(x)) if x[i] != y[i]])(s1, s2))`

Stacks lambda functions and assigns a larger lambda call to `ret`, avoiding recomputation while keeping the solution concise. First solution where I discovered the power of using a lambda function to "store" and use variables in my One-Line-Leets

### Problem [#3226](https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal) - Number of Bit Changes to Make Two Integers Equal
Original solution : `return str(bin(n^k)).count('1') if n - (n&k) - (n^k) == k - (n&k) else 0 if n == k else -1`

Optimised solution : `return str(bin(n^k)).count('1') if n - (n^k) == k else -1`

I like this solution a lot because it uses clever bit manipulation to form an elegant, efficient solution. Let's look at why it works : 

`n&k` represents the bits in `n` and `k` that are the same. We can just ignore these bits entirely, hence they are subtracted from both. This isn't entirely necessary since we're subtracting on both sides, but when I was drawing binary numbers on my whiteboard to figure this problem out, it was immensely helpful.

Now, we're left with residuals of `n` and `k`, comprising only of the digits between them that are different. `n^k` represents the bits that are different between the two numbers. Since the question requires that we only change `1`s in `n` to `0`s and not the other way round, this must mean that if it is possible to transform `n` to `k`, subtracting the differing bits (essentially converting all ones to zeroes) should result in `k` itself! That's why we check if `n - n^k == k`!

If this is true (we *can* transform `n` into `k`), then the number of bits we changed is the number of ones in the differing bits, so we do `str(bin(n^k)).count('1')`. If there are no differing bits, we return `0`. If both of these cases are not true, then it is not possible to convert `n` to `k`, hence we return `-1`

In actuality, the solution can be made much simpler in two ways. By removing the redundant subtractions of `n&k` on both sides, and the unecessary check to see if the values are equal (`...count('1')` would return 0 in this case anyways). This results in `return str(bin(n^k)).count('1') if n - (n^k) == k else -1`, which ends up beating 100% of submissions in both runtime (0ms) and memory (12.30MB) according to LeetCode.

I love the elegance of this solution and how simple logic gates are super useful and efficient in solving this problem!

### Problem [#1752](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated) - Check if Array Is Sorted and Rotated
`return (lambda i: nums[i:] + nums[:i] == sorted(nums))((next((i for i in range(1, len(nums)) if nums[i] < nums[i-1]), 0)))`

This solution is interesting as it uses a generator expression inside `next()` to find the first index where the array starts to decrease.

It then passes said index (or 0 if none are found) into a lambda expression, which reverses a potential array rotation about this index, and checks if this reversed rotation results in a sorted array.

Alternatively, the lambda argument could've been written like so : `(([i for i in range(1, len(nums)) if nums[i] < nums[i-1]] + [0])[0])`. But this would have to traverse the whole array and find indices where it starts decreasing. The generator and `next` allow for lazy evaluation, removing the need to traverse the entire array by breaking at the first match, making the algorithm faster overall.

The latter, unoptimised approach is what I've used in the past for numerous questions (such as [#3438 - Find Valid Pair of Adjacent Digits in String](./codes/3438.py)), but using generators and next() is a lot cleaner and more performant.

In general, constructions of the form : `([... for ... in ...] + [<default>])[0]` can be turned into `next((... for ... in ...), <default>)`. It significantly improves performance when avg case computation << worst case (i.e. where it is possible to lazy eval / break early rather than compute the whole list).
