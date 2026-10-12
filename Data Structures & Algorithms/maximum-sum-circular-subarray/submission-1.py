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
        
'''
Since its a circular array, we can wrap back around or its a subarray in the contiguous string

If its a subarray in the contiguous string, then we can just kadane's algorithm, however if we need to wrap backaround, we can find the subarray the generates the minimum value and subtract it from the total, then you the wrapped subarray
- If 2 numbers added together are positive, we would want to keep them, however if the future elements made this subarray negative, then this block is unoptimal for reaching a maxSum since including it would only decrease the max - this does not mean we remove every element for consideration

-2,4,-5,4,-5,9,4

- here -2,4,-5 would yield a -3, however -2,4 is still a valid chain to consider in the wrap around - so since -5 < -3, we keep the -5 and start a new subarray from there for min, then continue to -5 + 4 -5, which is -6, 9 - (-6) = 15

[-2, 4] | [-5, 4, -5] | [9, 4]
 prefix     middle       suffix

total - middle = prefix+suffix

If bestMax < 0 that means it was an array of negative numbers only, so return the lowest negative value (closest to 0)

Check whether bestMax or total - bestMin produces a larger value, so contiguous subarray or prefix+suffix
'''
