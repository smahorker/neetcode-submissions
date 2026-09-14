class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderInd = { c : i for i, c in enumerate(order)}
        
        def inOrder(w1, w2):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    return orderInd[c1] < orderInd[c2]
            return len(w1) <= len(w2)
        
        for i in range(len(words) - 1):
            if not inOrder(words[i], words[i+1]):
                return False
        return True