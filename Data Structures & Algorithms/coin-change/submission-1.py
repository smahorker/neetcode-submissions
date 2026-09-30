class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1


'''
The natural instinct is: "grab the biggest coin that fits, repeat." For 6 with [1, 3, 4], greedy picks 4 + 1 + 1 = 3 coins. But 3 + 3 = 2 coins is better.


tar = 6
dp[6]
[1,3,4]

Suppose we're at a = 5. We're building dp[5], the fewest coins needed to make exactly 5. For each coin c, we compute the complement 5 - c, the amount still left to build after placing that coin.

Say c = 3. The complement is 5 - 3 = 2, so we look at dp[2]. That cell was already finalized on an earlier iteration, since we fill the table in increasing order and tried every coin on amount 2 back then. It holds either the fewest coins needed to make 2, or the sentinel(amt+1 placeholder) if 2 is unreachable.

If it's a real count, then using coin 3 gives a candidate of 1 + dp[2]: one coin (the 3) plus the coins needed for 2. We compare that to the current dp[5] and keep the smaller. If dp[2] is the sentinel, the candidate is larger than the sentinel, so min ignores it.

Because dp[2] will never change again, we can build on it safely.

Code
Create dp array to hold minimum coins it takes to reach that amount

Reaching a value of 0 takes 0 coins, base case

Loop through all the values in amount, we are going to try each coin on these amounts to see whats the minimum value to build it
- Take amt 5 for example and try 6-1, 6-3, 6-4 and see if we've already computed the complement in our dp array which holds min coins to build an amt - the remaining amt is what we want to build, so dp[5], dp[3], and dp[2] is what we'd look at because dp[i] stores the minimum amount of coins to build that amount

Check whether the complement is non negative, otherwise it overshoots and we cant add the current coin to our min coins we are trying to compute
- 5 - 6 = -1, so we can't use a curr coin of 6 cause it overshoots

Compute the complement and add 1 to indicate we are adding the current coin - Curr coin + coins it takes to build complement, since we are checking all available coins from our input, we need to compare to see if we've found a more efficient way in the past

- 6-1 = dp[5], dp[5] was computed in the previous iteration as 2, so dp[6] = min(dp[6], 1 + 2) = 3, since dp[i ] wasnt assigned to anything yet we set 
dp[6] = 3 - which sets a baseline for dp[6]

- 6 - 3 = dp[3], dp[3] = 1, dp[6] = min(dp[6], 1+1) = 2, which means we update dp[6] to the new min

- 6 - 4 = dp[2], d[2] = 2, dp[6] = min(dp[6], 1+2) = 2 - using coin 3 on amount 6 was more efficient, so we kept 2 even though the number 4 was higher

Since 6 was our target and it did get updated, so we found a valid complement that we built on earlier - built on dp[5], dp[3], and dp[2] in our example, we can return dp[amount] which stored the minimum coins it took to build amount, else return -1
'''