# One Line LeetCode Solutions

I like challenging myself to solve LeetCode problems in one single line. Code Golf : Line Edition

This game of mine started a few years ago when I would stumble upon LeetCode problems that had unsuspecting elegant solutions that could fit in just one return statement. I wasn't intetionally seeking out solutions that consisted of a single expression. However, my interest in trying to find such one-line solutions piqued when I began learning functional programming in Racket/Scheme at the University of Waterloo, and now it's become a personal challenge of mine.

Goal : `[ "$(ls codes | wc -l)" -eq "$(grep -e "^ *return" codes/*.py | wc -l)" ] && echo "Equal" || echo "Not equal"` outputs "Equal"

---

## Rules : 
- Code must be one single line (One expression)

While `x=1; y=2; return x+y` is technically one line, for the spirit of the challenge this doesn't count as it is three "expressions"

However, while `return max(list(map(lambda pair: pair[0] ^ pair[1], filter(lambda pair: abs(pair[0]-pair[1]) <= min(pair[0],pair[1]), list(set([(nums[i], nums[j]) for i in range(len(nums)) for j in range(i, len(nums))]))))))` is a mouthful and a half, it is one single "expression". And so, it counts. (btw this is indeed a solution to [Problem #2932](https://leetcode.com/problems/maximum-strong-pair-xor-i/))

All solutions are titled by their corresponding problem number. File \<problem-number\>.py (`^[0-9]*.py$`) contains the problem description, a link to the problem, and my one line solution, sometimes with comments.

Disclaimer : These solutions are usually **extremely** inefficient. Sometimes they shine though.

---

## Longest and Shortest Solutions :
Metric : Convert all variable (and parameter) names to single characters, remove as much whitespace as possible, measure number of characters in the return statement (including the word `return`)

Yes, the code logic itself could be made longer (or *shorter?*) to artificially modify the result, but I'll try not to intentionally write extremely long code :P

### Shortest Solution : 
[#1025](https://leetcode.com/problems/divisor-game/) `divisorGame(self, n)` : ~~13~~ 12 Characters

Original : `return n%2==0`

~~This can even be made one character shorter in C like so :~~ `return ~n&1;` ~~. Unlike C, 0 and 1 aren't considered "boolean types" in Python, so this won't work as a Python solution. All non-zero integers are treated as True and zero, False when used in a boolean expression, but alone, they are integers. LeetCode explicitly requires a boolean returned for this question.~~

New : `return n%2<1`

### Longest Solution : 
[#2423](https://leetcode.com/problems/remove-letter-to-equalize-frequency) `equalFrequency(self, w)` : 265 Characters

`return(lambda a,b:min(a,key=a.count)==max(a,key=a.count)or min(b,key=b.count)==max(b,key=b.count))((lambda l:(lambda x:l[:l.index(x)]+l[l.index(x)+1:])(max(l,key=l.count)))(list(w)),(lambda l:(lambda x:l[:l.index(x)]+l[l.index(x)+1:])(min(l,key=l.count)))(list(w)))`

---

## Solutions I find interesting :

### Problem [#2248](https://leetcode.com/problems/intersection-of-multiple-arrays) - Intersection of Multiple Arrays
`return sorted(reduce(lambda x,y:[i for i in x if i in y],nums))`

Uses `reduce()` which works like `foldr`, accumulating results and iterating through nums to find the intersection. First solution where I tried to incorporate my (then) newly gained knowledge of the "fold" Abstract List Functions.

### Problem [#1790](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal) - Check if One String Swap Can Make Strings Equal
`return (lambda ret: False if (len(s1) != len(s2)) or (len(ret) not in {0,2}) else len(ret) == 0 or (s1[ret[0]] == s2[ret[1]] and s1[ret[1]] == s2[ret[0]]))((lambda x, y: [i for i in range(len(x)) if x[i] != y[i]])(s1, s2))`

Stacks lambda functions and assigns a larger lambda call to `ret`, using its lambda nature to avoid recomputation while keeping the solution concise. First solution where I discovered the power of using a lambda function to "store" and use variables in my One-Line-Leets

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

The latter, unoptimised approach is what I've used in the past for numerous questions (such as #3438 - Find Valid Pair of Adjacent Digits in String).

## Problems You'll Find in this Repository : 

Below is a table indicating problems I've solved and explained in one line out of all the files I've uploaded to this repository. The problem title is a link to the problem for you to try it out yourself.

My solutions can be found under `codes/` named `<problem-number>.py` or by clicking on "Problem Number" below, and explanations under `explanations/` named `<problem-number>.md`

**Legend :**
- ✅ Complete
- ❌ Incomplete
- ⏱️ Time Limit Exceeded
- 💥 Memory Limit Exceeded

| Problem Number          | Problem Title (Leetcode Redirect)                                                                       | Solved | Explained |
|-------------------------|---------------------------------------------------------------------------------------------------------|--|---|
| [0067](codes/0067.py)   | [Add Binary](https://leetcode.com/problems/add-binary/)                                                 |✅|❌|
| [0169](codes/0169.py)   | [Majority Element](https://leetcode.com/problems/majority-element/)                                     |✅|❌|
| [0190](codes/0190.py)   | [Reverse Bits](https://leetcode.com/problems/reverse-bits/)                                             |✅|❌|
| [0191](codes/0191.py)   | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)                                     |✅|✅|
| [0229](codes/0229.py)   | [Majority Element II](https://leetcode.com/problems/majority-element-ii/)                               |✅|❌|
| [0231](codes/0231.py)   | [Power of Two](https://leetcode.com/problems/power-of-two/)                                             |✅|❌|
| [0268](codes/0268.py)   | [Missing Number](https://leetcode.com/problems/missing-number/)                                         |✅|❌|
| [0338](codes/0338.py)   | [Counting Bits](https://leetcode.com/problems/counting-bits/)                                           |✅|❌|
| [0372](codes/0372.py)   | [Super Pow](https://leetcode.com/problems/super-pow/)                                                   |✅|❌|
| [0412](codes/0412.py)   | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)                                                   |✅|❌|
| [0434](codes/0434.py)   | [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/)         |✅|❌|
| [0476](codes/0476.py)   | [Number Complement](https://leetcode.com/problems/number-complement/)                                   |✅|❌|
| [0551](codes/0551.py)   | [Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/)               |✅|❌|
| [0575](codes/0575.py)   | [Distribute Candies](https://leetcode.com/problems/distribute-candies/)                                 |✅|❌|
| [0648](codes/0648.py)   | [Replace Words](https://leetcode.com/problems/replace-words/)                                           |✅|❌|
| [0680](codes/0680.py)   | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)                               |✅|❌|
| [0693](codes/0693.py)   | [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/)|✅|❌|
| [0821](codes/0821.py)   | [Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/)     |✅|❌|
| [0898](codes/0898.py)   | [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/)                     |⏱️|❌|
| [0922](codes/0922.py)   | [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)                       |✅|❌|
| [0977](codes/0977.py)   | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)                   |✅|❌|
| [0989](codes/0989.py)   | [Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/)             |✅|✅|
| [1009](codes/1009.py)   | [Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/)           |✅|❌|
| [1025](codes/1025.py)   | [Divisor Game](https://leetcode.com/problems/divisor-game/)                                             |✅|❌|
| [1266](codes/1266.py)   | [Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)     |✅|❌|
| [1295](codes/1295.py)   | [Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) |✅|❌ |
| [1317](codes/1317.py)   | [Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) |✅|✅|
| [1365](codes/1365.py)   | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) |✅|❌ |
| [1374](codes/1374.py)   | [Generate a String With Characters That Have Odd Counts](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/)|✅|❌|
| [1460](codes/1460.py)   | [Make Two Arrays Equal by Reversing Sub-arrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/)|✅|❌|
| [1486](codes/1486.py)   | [XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)                   |✅|❌|
| [1704](codes/1704.py)   | [Determine if String Halves Are Alike](https://leetcode.com/problems/determine-if-string-halves-are-alike/)                  |✅|❌|
| [1752](codes/1752.py)   | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)                  |✅|❌|
| [1790](codes/1790.py)   | [Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/) |✅|❌|
| [1805](codes/1805.py)   | [Number of Different Integers in a String](https://leetcode.com/problems/number-of-different-integers-in-a-string/)          | ✅ | ✅   |
| [1812](codes/1812.py)   | [Determine Color of a Chessboard Square](https://leetcode.com/problems/determine-color-of-a-chessboard-square/)              |✅|❌|
| [1835](codes/1835.py)   | [Find XOR Sum of All Pairs Bitwise AND](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/)                |✅|❌|
| [1876](codes/1876.py)   | [Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) |✅|❌|
| [1952](codes/1952.py)   | [Three Divisors](https://leetcode.com/problems/three-divisors/)                                         |✅|❌|
| [1980](codes/1980.py)   | [Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/)                   |✅|❌|
| [2000](codes/2000.py)   | [Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word/)                         |✅|❌|
| [2006](codes/2006.py)   | [Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/)   |✅|❌|
| [2022](codes/2022.py)   | [Convert 1D Array Into 2D Array](https://leetcode.com/problems/convert-1d-array-into-2d-array/)         |✅|✅|
| [2032](codes/2032.py)   | [Two Out of Three](https://leetcode.com/problems/two-out-of-three/)                                     |✅|❌|
| [2057](codes/2057.py)   | [Smallest Index With Equal Value](https://leetcode.com/problems/smallest-index-with-equal-value/)       |✅|✅|
| [2089](codes/2089.py)   | [Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array/)            |✅|❌|
| [2108](codes/2108.py)   | [Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)      |✅|❌|
| [2114](codes/2114.py)   | [Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)      |✅|❌|
| [2161](codes/2161.py)   | [Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/)          |✅|❌|
| [2185](codes/2185.py)   | [Counting Words With a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/) |✅|✅|
| [2206](codes/2206.py)   | [Divide Array Into Equal Pairs](https://leetcode.com/problems/divide-array-into-equal-pairs/)           |✅|❌|
| [2239](codes/2239.py)   | [Find Closest Number to Zero](https://leetcode.com/problems/find-closest-number-to-zero/)               |✅|❌|
| [2248](codes/2248.py)   | [Intersection of Multiple Arrays](https://leetcode.com/problems/intersection-of-multiple-arrays/)       |✅|❌|
| [2255](codes/2255.py)   | [Count Prefixes of a Given String](https://leetcode.com/problems/count-prefixes-of-a-given-string/)     |✅|❌|
| [2259](codes/2259.py)   | [Remove Digit From Number to Maximize Result](https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/)    |✅|❌|
| [2364](codes/2364.py)   | [Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs/)                   | 💥   |❌|
| [2418](codes/2418.py)   | [Sort the People](https://leetcode.com/problems/sort-the-people/)                                       |✅|❌|
| [2423](codes/2423.py)   | [Remove Letter To Equalize Frequency](https://leetcode.com/problems/remove-letter-to-equalize-frequency/)                    |✅|❌|
| [2455](codes/2455.py)   | [Average Value of Even Numbers That Are Divisible by Three](https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/) |✅|❌|
| [2491](codes/2491.py)   | [Divide Players Into Teams of Equal Skill](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/)          |✅|❌|
| [2535](codes/2535.py)   | [Difference Between Element Sum and Digit Sum of an Array](https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/) |✅|❌|
| [2549](codes/2549.py)   | [Count Distinct Numbers on Board](https://leetcode.com/problems/count-distinct-numbers-on-board/)       |✅|❌|
| [2553](codes/2553.py)   | [Separate the Digits in an Array](https://leetcode.com/problems/separate-the-digits-in-an-array/)       |✅|❌|
| [2570](codes/2570.py)   | [Merge Two 2D Arrays by Summing Values](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/)                |✅|❌|
| [2579](codes/2579.py)   | [Count Total Number of Colored Cells](https://leetcode.com/problems/count-total-number-of-colored-cells/)                    |✅|❌|
| [2651](codes/2651.py)   | [Calculate Delayed Arrival Time](https://leetcode.com/problems/calculate-delayed-arrival-time/)         |✅|❌|
| [2652](codes/2652.py)   | [Sum Multiples](https://leetcode.com/problems/sum-multiples/)                                           |✅|❌|
| [2656](codes/2656.py)   | [Maximum Sum With Exactly K Elements](https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/)                    |✅|❌|
| [2678](codes/2678.py)   | [Number of Senior Citizens](https://leetcode.com/problems/number-of-senior-citizens/)                   |✅|❌|
| [2710](codes/2710.py)   | [Remove Trailing Zeros From a String](https://leetcode.com/problems/remove-trailing-zeros-from-a-string/)                    |✅|❌|
| [2716](codes/2716.py)   | [Minimize String Length](https://leetcode.com/problems/minimize-string-length/)                         |✅|❌|
| [2788](codes/2788.py)   | [Split Strings by Separator](https://leetcode.com/problems/split-strings-by-separator/)                 |✅|❌|
| [2798](codes/2798.py)   | [Number of Employees Who Met the Target](https://leetcode.com/problems/number-of-employees-who-met-the-target/)              |✅|❌|
| [2828](codes/2828.py)   | [Check if a String Is an Acronym of Words](https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/)          |✅|❌|
| [2864](codes/2864.py)   | [Maximum Odd Binary Number](https://leetcode.com/problems/maximum-odd-binary-number/)                   |✅|✅|
| [2932](codes/2932.py)   | [Number of Employees Who Met the Target](https://leetcode.com/problems/number-of-employees-who-met-the-target/)              |✅|❌|
| [2980](codes/2980.py)   | [Check if Bitwise OR has Trailing Zeros](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/)              |✅|❌|
| [3019](codes/3019.py)   | [Number of Changing Keys](https://leetcode.com/problems/number-of-changing-keys/)                       |✅|❌|
| [3042](codes/3042.py)   | [Count Prefix and Suffix Pairs I](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/)       |✅|❌|
| [3079](codes/3079.py)   | [Find the Sum of Encrypted Integers](https://leetcode.com/problems/find-the-sum-of-encrypted-integers/) |✅|❌|
| [3083](codes/3083.py)   | [Existence of a Substring in a String and its Reverse](https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/) |✅|❌|
| [3110](codes/3110.py)   | [Score of a String](https://leetcode.com/problems/score-of-a-string/)                                   |✅|✅|
| [3136](codes/3136.py)   | [Valid Word](https://leetcode.com/problems/valid-word)                                                  |✅|❌|
| [3151](codes/3151.py)   | [Special Array I](https://leetcode.com/problems/special-array-i/)                                       |✅|❌|
| [3226](codes/3226.py)   | [Number of Bit Changes to Make Two Integers Equal](https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/) |✅|❌|
| [3340](codes/3340.py)   | [Check Balanced String](https://leetcode.com/problems/check-balanced-string/)                           |✅|❌|
| [3438](codes/3438.py)   | [Find Valid Pair of Adjacent Digits in String](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/)  |✅|❌|
| [3442](codes/3442.py)   | [Maximum Difference Between Even and Odd Frequency](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)      |✅|❌ |
| [3683](codes/3683.py)   | [Earliest Time to Finish One Task](https://leetcode.com/problems/earliest-time-to-finish-one-task/)     |✅|❌|
| [3684](codes/3684.py)   | [Maximize Sum of At Most k Distinct Elements](https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/)    |✅|❌|
| [3688](codes/3688.py)   | [Bitwise Or of Even Numbers in an Array](https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/)              |✅|❌|
| [3689](codes/3689.py)   | [Maximum Total Subarray Value I](https://leetcode.com/problems/maximum-total-subarray-value-i/)         |✅|❌|
| [3692](codes/3692.py)   | [Majority Frequency Characters](https://leetcode.com/problems/majority-frequency-characters/)           |✅|❌|