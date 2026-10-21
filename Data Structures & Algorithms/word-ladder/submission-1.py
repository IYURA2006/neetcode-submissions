from collections import deque
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        alphabet = string.ascii_lowercase  
        visited  = set()

        wordList = set(wordList)

        def bfs (word):
            queue = deque()
            queue.append(word)
            visited.add(word)

            dist = 1
            while queue:

                for i in range(len(queue)):

                    word = queue.popleft()

                    
                    if word == endWord:
                        return dist

                    for i in range(len(word)):
                        for letter in alphabet:
                            if letter == word[i]:
                                continue
                            res = (word[:i] + letter + word[i + 1 : ])
                            if res in wordList and res not in visited:
                                queue.append(res)
                                visited.add(res)
                dist += 1
            
            return 0
        return bfs(beginWord)
          
