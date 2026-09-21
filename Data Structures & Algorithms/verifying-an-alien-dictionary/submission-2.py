class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha = {c : i for i, c in enumerate(order)} 

        def inOrder(w1, w2):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    return alpha[c1] < alpha[c2]
            return len(w1) <= len(w2)
        
        return all(inOrder(words[i], words[i+1]) for i in range(len(words) - 1))
                
