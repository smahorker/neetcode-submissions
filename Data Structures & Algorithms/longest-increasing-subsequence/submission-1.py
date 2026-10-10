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

'''