class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]


'''
Same sol as house robber 1, but since its a cycle, we cant use house 1 or house 2, so you can functionally skip these by starting from idx 1 and going til the end or starting from idx 0 until nums-1 because you can't rob either one of these houses since they are adjacent to each other, so you compare whether skipping one or the other leads to the higher solution
'''