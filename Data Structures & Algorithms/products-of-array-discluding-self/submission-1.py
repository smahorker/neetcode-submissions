class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

'''
Product of array is is product of everything to the left and right of it, except itself, so perform two passes, first one we calculate product of everything to the left of the current value, then second pass calculates everything to the right of it

Use prefix state var to track the product thus far, default to 1 because its itself, we first update the result arr and then only update the prefix value, by doing so we are essentially skipping the current value from being accounted for in res by only updating prefix after we update res

After we perform this skip, then we move onto the next iteration, where we use this product and update res, which once again skips over considering the current value and only updates prefix accordingly after

This process skips the last value in the array, update then compute = skip and skip last value

A prefix is a product up til that point on the left of idx and the postfix is the product of the values up til that point at the right of the idx and if we combine them, it combines both sides excluding the current element

1,2 - 3 - 4,5 - combining 1,2 and 4,5 we get 40, if we combine both the prefix and postfix 

for 1, we only care whats on the right of it, so postfix wont update the value til the final iteration
'''