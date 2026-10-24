class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {order[i]:i for i in range(len(order))}
        print(dictionary)
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            
            for j in range(len(word1)):
                #first word is bigger
                if j == len(word2):
                    return False
                
                if word1[j] != word2[j]:
                    if (dictionary[word1[j]] > dictionary[word2[j]]):
                        return False
                    #if they are in the rigth order we need to break
                    break

                
        
        return True
