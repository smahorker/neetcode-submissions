class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        currMin = currMax = res = nums[0]

        for x in nums[1:]:
            candidates = (x, currMin*x, currMax*x)
            currMax = max(candidates)
            currMin = min(candidates)
            res = max(res, currMax)
        return res


'''
For each number we explore in the input, its either x alone (fresh start), x*curMin, or x*curMax 

Cant just start currMin, currMax, and res at 0 because if its a list with a single negative element, then the 0 will evaluate higher than the negative value for currMax

- curMin*x could become curMax or curMax*x could become curMin
-- num = -4,  curMin=-5 -5*-4 =20, curMax=5 5*-4 = -20 - so in the next iteration the curMax is 20 and curMin is -20 because of the negative signs

When we encounter a 0, all candidates are 0 after (0, currMin*0, currMax*0), in the next iteration 
- positive case: candidates = (4, 0*4, 0*4) - so this evals to 4 and then performs the check on this single element subarr
- negative case: candidates = (-4, 0*-4, 0*-4) - this evals to 0, which cant be a new res, but obviously we still do the currMin, currMax, and res checks

Cant compare res = (res, candidates) because candidates is a tuple and res is an an int
'''
