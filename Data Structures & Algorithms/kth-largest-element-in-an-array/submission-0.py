class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max = [-n for n in nums]
        heapq.heapify(max)

        for _ in range(k - 1):
            heapq.heappop(max)
        
        return -(max[0])
