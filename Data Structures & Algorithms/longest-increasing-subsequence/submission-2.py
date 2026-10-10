class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


'''
dp[i] = the length of the longest increasing subsequence that ends exactly at index i

To compute dp[i], look at every earlier index j < i

If nums[j] < nums[i], then nums[i] can extend the best subsequence ending at j, giving length dp[j] + 1

If nothing before i is smaller, nums[i] starts a new subsequence of length 1.

We check dp[i] and d[j]+1 because we may have found a larger subsequence earlier in our j search
j = 2 - found 2+1=3
j = 3 - found 1+1=2

Compare dp[i] with d[j] + 1 because we may have found a higher subsequence earlier in the search

Looking from j to i, for example 0 to 4 because dp[4] represents the largest subsequence we found of the first 4 elements, and lets say idx 3 yielded the largest subsequence,
which means idx 4 < idx 3, otherwise idx 4 would have been included

- When we go to idx 5, if idx 5 > idx 3, then dp[j] where j is 3 tells us the longest subsequence until that point of the array, so we check dp[i] vs dp[3] +1, and dp[5] becomes dp[3] + 1, then when check dp[4], even if nums[4] < nums[5], we see when we compare max(dp[5], dp[4] + 1) we see that dp[5] is larger and sustain that value
'''