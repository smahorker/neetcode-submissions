'''
Create a list of buckets of size of the array, each bucket represents the frequency that the element apepars,
count the values and place them into a hashmap, 
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq =[[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    
    '''
    for i in range(start, stop, step)
        - stop is exclusive so we skip over idx 0 since anything of freq 0 doesnt matter, we would do -1 in order to include this, the start however is inclusive so we would need to do -1

'''