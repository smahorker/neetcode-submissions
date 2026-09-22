class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha = {c : i for i, c in enumerate(order)} 

        def inOrder(w1, w2):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    return alpha[c1] < alpha[c2]
            return len(w1) <= len(w2)
        
        return all(inOrder(words[i], words[i+1]) for i in range(len(words) - 1))
                
'''
Create a dictionary of provided alphabet, mapping char : idx, this way we have a lexicological mapping that we can compare against

We need to compare whether the list of words are in order, so we need to compare the first words to the next

Compare each word character by character, a word that is a prefix must appear earlier in the list

Zip both words, if there is spillage then it gets truncated - the length of the tuple of pairs is based on the shortest word - 4,6 = 4 pairs

We zip during the loop and bind c1 to w1 character and c2 to w2 character, check whether they are not equal and if so we need to use our dictionary to see if there is a mismatch against our dictionary, return the comparison, if its true then we continue to the next word, since our return statement is based on all being true

return true only if all comparisons returned true, make sure to only loop to the 2nd last word because of i + 1
'''