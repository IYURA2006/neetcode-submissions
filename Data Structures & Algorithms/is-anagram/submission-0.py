from collections import defaultdict

#dictionary letter - freq
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = defaultdict(int)
        word2 = defaultdict(int)

        
        for i in list(s):
            word1[i] += 1

        for i in list(t):
            word2[i] += 1
    
        return word1 == word2