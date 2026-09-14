'''
Create 2 hashmaps that count the characters present, if the characters hashmaps are the
same then they are anagrams


'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        CountS, CountT = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            CountS[s[i]] += 1
            CountT[t[i]] += 1
        
        if CountS == CountT:
            return True
        else:
            return False
