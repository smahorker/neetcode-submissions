class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            a = min(heights[r], heights[l]) * (r-l)
            res = max(res, a)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r-= 1
        return res
                