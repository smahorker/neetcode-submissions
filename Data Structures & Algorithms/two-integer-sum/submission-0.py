class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in prevMap:
                return [prevMap[comp], idx]
            prevMap[num] = idx