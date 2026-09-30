class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                bt(i+1, path)
                path.pop()
        
        bt(0, [])
        return res
                

'''
Start represents the index, not the actual number

We dont want to skip the first time we see the number, since thats a guaranteed non duplicate, however if we increment i and the number stays the same as the one we saw in the previous index, then move past this iteration in the loop to continue until we find a unique number or the loop returns
'''