class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            currSum = max(num, currSum+num)
            maxSum = max(currSum, maxSum)
        return maxSum
'''
If the current running sum is negative, it can only drag you down so drop the subarray, but if its positive, keeping it can only help so extend

[x,x,x, 4] - the initial value must be positive otherwise it would have been dropped and any positive value will be beneficial
- Think of the chunk of Xs as a singular value of 2 - since its a contigious array they are all in a group  - in order to process 4, its either keep it all or get rid of it all and since the prev subarr is positive the chunk can only be helpful

- Starting with a negative value can never be beneficial, if the list is fully negative the smallest number will just choose itself num in the max(num,curSum+num) check and max updates to it on th next line
'''