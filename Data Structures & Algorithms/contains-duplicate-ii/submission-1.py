from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        dictionary = defaultdict(list)
        for i in range(len(nums)):
            dictionary[nums[i]].append(i)
        
        for val in dictionary.values():
            if len(val) > 1:
                for i in range(len(val) - 1):
                    if abs(val[i+ 1] - val[i]) <=k:
                        return True
        return False
        '''

        left = 0
        visited = set()

        for right in range(len(nums)):
            #check if right - left <=k
            if right - left > k:
                visited.remove(nums[left])
                left += 1
            
            if nums[right] in visited:
                return True
            
            visited.add(nums[right])
        
        return False
               

