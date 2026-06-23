class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seq = set(nums)

        for num in nums:
            if (num - 1) not in seq:
                length = 1
                while (num + 1) in seq:
                    length += 1
                    num += 1
                res = max(res, length)

        return res