class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        CurEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == CurEnd:
                jumps += 1
                CurEnd = farthest
                if CurEnd >= (len(nums) - 1):
                    break
        
        return jumps