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

'''
Once we've verified a subarray is valid, once we hit an invalid case, we can shift our ptr there because we met the stopping condition and every value inside the subarr will never yield a higher max

4, 2, 10, 7, 8, 8

- max = 5, if we shift left window to 2, then the stopping condition is still there but our max = 4, so we can just move to 8 - so once a window is invalid, we dont need to check inside it

Cases:
Sign flipped - extend curr by 1
Sign did not flip - 7<8<9, however 8<9 is a valid comparison for the next subarr we are finding
Equal elements - no valid, so start at length 1, 7<8=8, so we start at the last 8

We dont need to manage left and right ptrs because we can jump to the end and dont need to return the valid subarr

Track the best window, cur len of window, and PrevSign - which we compare against the current sign to see if it flipped

Sign variable having 1 representing >, -1 representing <, and 0 representing =

Loop through the values starting at 1, since we know the first standalone element is valid until n

Check whether the i > i-1, if so sign = 1, check whether i < i-1, if so sign = -1, otherwise its equal so sign = 0

Now that we have the current sign, we can compare it against the prev sign

- if signs did not flip, that means the last 2 values were valid since 8<9 is a valid sequence in a subarr
- if the values were equal, then only the last value is valid because 8=8 is not a valid starting spot
- if the signs flipped we just increment by 1

However when i = 1, sign != prevsign since we base our sign on 0, so that an invalid comparison cant happen - even though prevsign is 0, we first check whether sign == 0, because we dont care if the prevsign was equal or not 
- So we default to the else case of cur = 2 which is valid, we also default to this case when saw an equal sign in the previous iteration 4=4<6, so cur becomes 2, or when we encountered a non flipped sign earlier in the array 4<5<6
-- In either of these cases, neither sign == 0 or sign == -prevsign when comparing the 4<6 or the 5<6 part, but they are still valid so we need to set cur to 2 - in the case of 4<5<6, cur was already 2 from the 4<5, but since 5<6 is also valid it stays

'''