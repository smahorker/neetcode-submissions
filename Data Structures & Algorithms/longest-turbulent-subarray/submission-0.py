class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        best = 1
        cur = 1
        PrevSign = 0 # 0 for eq, 1 for pos, -1 for neg

        for i in range(1, n):
            if arr[i] > arr[i-1]:
                sign = 1
            elif arr[i] < arr[i-1]:
                sign = -1
            else:
                sign = 0
        
            if sign == 0:
                cur = 1
            elif sign == -PrevSign:
                cur += 1
            else:
                cur = 2
        
            PrevSign = sign
            best = max(best, cur)

        return best