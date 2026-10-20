class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        first = 0
        second = 0

        res = []
        while first < len(firstList) and second < len(secondList):
            startF = firstList[first][0]
            endF = firstList[first][1]

            startS = secondList[second][0]
            endS = secondList[second][1]


            a = max(startS, startF)
            b = min(endS, endF)

            if a<=b :
                res.append([a,b])

            if endS < endF:
                second += 1
            else:
                first += 1
            
            
        
        return res
