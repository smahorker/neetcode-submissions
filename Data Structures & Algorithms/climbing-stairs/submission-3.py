class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        

'''
bottom up

There are 2 possible moves in order to arrive at n, you either take 1 step at n-1 or 2 steps at n-2

Base case
1 step has 1 way and 2 steps have 2 ways of getting there - implicit

dp[i] holds the amount of ways to reach step i, create an array big enough to hold 0 to n moves and build on it
 
Since we've already stored the last 2 answers, we can use that to accumulate n, because those 2 moves are the only ways to reach n

There are 2 moves, either a 1 jump or a 2 jump toward n, the number of paths where we 1 jump are the accumulated paths at n-1, the number of paths where we 2 jump are the accumulated paths at n-2 - we use dp to accumulate these paths are store them

- We know that idx 0 has no jumps, so we dont store that in the dp, but we need to go from idx 0 to idx 1 or idx 2 which is mappable

Now that we have 2 verified accumulations, we met the minimum requirement for up til n to aggregate

for example at i = 3, the number of ways to get to n-1 is 2 and the number of ways to get to n-2 is 1, so to account for the 1 jump path and the 2 jump path to reach n we add them together

Every way to reach n ends with either a jump from n-1 or a jump from n-2. So the number of ways to reach n equals the number of ways to reach n-1 (each finished off with a +1 jump) plus the number of ways to reach n-2 (each finished off with a +2 jump). Since these are the only two valid final moves, and they can't both happen at once, we add them to get the total.

[1,1,1] → [1,1,1,1]
[1,2]   → [1,2,1]
[2,1]   → [2,1,1]

[1,1] → [1,1,2]
[2]   → [2,2]

How many ways are there to get to n from n-1, well you would need to add a 1 to each path at n-1, how many ways to get to n-2, you need to add a 2 to each path - the number of paths relative to dp[n-1] or dp[n-2] isnt increasing, but we are appending a value at the end of them to simulate reaching n, since n-1 and n-2 are the only paths we add them and that is the total paths from the 2 jumps starting points

The addition (dp[n-1] + dp[n-2]) — just combining the sizes of two non-overlapping, complete groups
- those two groups are exhaustive (cover every possibility) and mutually exclusive (no overlap), summing their sizes gives the true total.
'''