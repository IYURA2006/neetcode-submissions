from collections import defaultdict
from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjlist = defaultdict(list)
        indegree = {}
        numCharacters = 0

        for word in words:
            for w in word:
                if w not in indegree:
                    indegree[w] = 0
                    numCharacters += 1

        for w in range(1, len(words)):
            #should be bigger if equal
            word2 = words[w]
            word1 = words[w-1]

            for l in range(len(word1)):
                if l > len(word2) - 1:
                    return ""
                

                if word1[l] != word2[l]:
                    adjlist[word1[l]].append(word2[l])
                    indegree[word2[l]] += 1
                    break
        
        print(adjlist)
        print(indegree)
        queue = deque()

        for key, value in indegree.items():
            if value == 0:
                queue.append(key)
        
        res = ""
        while queue:
            letter = queue.popleft()
            res += letter
            for next_letter in adjlist[letter]:
                indegree[next_letter] -= 1
                if indegree[next_letter] == 0:
                    queue.append(next_letter)

        print(numCharacters)
        if len(res) != numCharacters:
            return ""
        return res


