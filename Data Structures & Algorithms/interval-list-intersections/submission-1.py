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

            if endF < startS:
                first += 1
                continue
            
            if endS < startF:
                second += 1
                continue

            a = max(startS, startF)
            b = min(endS, endF)

            if endS < endF:
                second += 1
                firstList[first][0] = b
            else:
                first += 1
                secondList[second][0] = b
            
            res.append([a,b])
        
        return res
