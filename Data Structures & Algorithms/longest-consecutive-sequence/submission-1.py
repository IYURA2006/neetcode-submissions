class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        setnumbers = set()
        for item in nums: 
            setnumbers.add(item)
        
        longestSeq = float('-inf')
        for item in nums:
            #if -1 no, start of the seq
            if (item - 1) is not (setnumbers):
                x = 0
                while (item + x) in setnumbers:
                    x += 1
                    longestSeq = max(longestSeq, x)
    
        return longestSeq
