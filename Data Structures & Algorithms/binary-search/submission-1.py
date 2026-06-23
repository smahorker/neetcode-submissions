class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: # since we need to compare the final value to the target before it jumps past in traditional 2 ptrs we are comparing 2 values, but since we are searching for a target, we compare against itself
            mid = (r+l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        
        return -1