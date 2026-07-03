class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)

        n = min(len(word1), len(word2))
     
        res = []
        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])
        print(word1)
        if len(word1) > n:
            res.extend(word1[n:len(word1)+1])
        if len(word2) > n:
            res.extend(word2[n:len(word2)+1])
        
        return "".join(res)
   

        