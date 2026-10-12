class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        curMin = curMax = 0
        bestMin = float('inf')
        bestMax = float('-inf')

        for x in nums:
            total += x

            curMax = max(x, curMax + x)
            bestMax = max(bestMax, curMax)

            curMin = min(x, curMin + x)
            bestMin = min(curMin, bestMin)

        
        if bestMax < 0:
            return bestMax
        
        return max(bestMax, total - bestMin)
        

