from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = defaultdict(list)
        for self, other in trust:
            people[other].append(self)
        
        print(people)
        judge = -1
        for i in people:
            if len(people[i]) == n - 1:
                judge = i
        for x, trustee in people.items():
            if x != judge and judge in trustee:
                judge = -1
            print(i)
                
        return judge