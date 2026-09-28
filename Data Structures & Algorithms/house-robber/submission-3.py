class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]

'''
The dp array is a way of saving our work. dp[i] is the maximum profit we can make using houses 0 through i.

At each house we have two options: skip it or rob it.

Skip: If we skip house i, our best is whatever we had before, so dp[i] = dp[i-1].

Rob: If we rob house i, we can't build on dp[i-1], because that value might include the money from house i-1, and robbing both would set off the alarm. Instead we jump back to dp[i-2], the best profit using houses 0 through i-2. That subproblem never considers house i-1, so the adjacency rule is respected automatically. Our total is nums[i] + dp[i-2].

We compare the two options and keep the larger:

dp[i] = max(dp[i-1], nums[i] + dp[i-2])

Base cases: dp[0] = nums[0], and dp[1] = max(nums[0], nums[1]). The answer is dp[n-1].

The reason we don't use cost[i] + dp[i-1] even if we know we skipped a house previously, is because dp[i-1] and dp[i-2] hold the same values, so in order to handle the case that it was visited, we default to only using cost[i] + dp[i-2], which functionally gives us the same result at dp[i-1]
- When the previous house was skipped we can use dp[i-1] or dp[i-2] since we assigned dp[i-1] = dp[i-2] in the previous iteration when finding the max - so we skipped the previous house
- When the previous house wasn't skipped, we can only either skip this house or use the non adjacent idx, dp[i-2], so we see whether using the non adjacent idx with the current idx yields a higher value - which will always be true after a skip in the previous iteration, or whether the non adjacent idx + cost yields less than using the adjacent node
-- Seeing whether excluding the adajcent node leads to a higher output

[2, 1, 1, 2]

dp[0] = 2 dp[1] = 2
max(dp[i-1], cost[i] + dp[i-2])

dp[2]
- since we performed a skip at dp[1], we have to take the current house for dp[2] since both i-1 and i-2 are the same, adding anything will always evaluate to it being dp[i-2] being higher

dp[3]
- we have 2 options, using dp[i-1] or cost[i] + dp[i-2], dp[i-2] functions as excluding dp[i-1], so after adding both together we see that cost[i] = 2 and dp[1] = 2 so 2+2 = 4, store in dp[4] then return

The reason we use max when deciding dp[1] is because choosing the higher value will always lead to the greatest gain, also we only choose 1 of them as they are adjacent to each other
- If we perform a skip and [i-1] and [i-2] are the same, then we go to i, we use up [i-1], but we dont have to worry about the adjacent value (i+1) being force skipped and having a higher value because [i-2] stores the same value, so we can instead use that to serve as skipping over i
'''

