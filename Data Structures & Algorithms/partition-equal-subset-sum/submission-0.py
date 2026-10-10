class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp = [False] * (target+1)
        dp[0] = True
        
        for num in nums:
            for s in range(target, num-1, -1):
                if dp[s-num]:
                    dp[s] = True
        
        return dp[target]

'''
If the two subsets have equal sums, each must equal total / 2

If total is odd, the answer is immediately False

dp[s] = True means “I can make exactly s by picking some of the numbers I've seen."


----------------------------

nums = [1, 5, 11, 5]

Total = 22, so target = 11. The array dp has indices 0 through 11.


num = 1

Loop: s goes from 11 down to 1 (range(11, 0, -1))

only s=1 works, dp[1-1] = dp[0] = True, so dp[1] = True, which is valid since we used the 1

num = 5

Loop s goes from 11 down to 5

s = 6 works, dp[6-5] = dp[1] = True, so set dp[6] = True - 5+1 can build it

num = 11

s = 11 works, dp[11-11] = dp[0] = True, so set dp[11] = True

- Our stopping condition is met, but we still check the rest to see, so we still process num = 5 even though it does nothing

-----------------------

- We know target = total // 2, so if we build target using some subset, the list of remaining values has to be the total - target = target as well because
target+target = total

- Building a subset to see if we can find target, which we find by going through each number

When processing num = 5, we loop s from target down to 5. For each s, we check dp[s - 5]: if that total was reachable before, then adding this 5 makes s reachable. We update every s in that range, not just target, because those intermediate totals are needed by later numbers.
- If we go in knowing that dp[6] is valid, then dp[11-5] = dp[6] - we are essentially checking whether the complement exists in a sum we found previously
'''
