class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0 #first array
        right = 0 #second array

        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                left += 1
            else:
                temp = nums1[left] #current right need to placed 
                nums1[left] = nums2[right]
                right += 1
         
                i = left + 1
                while i <= m:
                    temp, nums1[i] = nums1[i], temp
                    i += 1
                m += 1
                left += 1

               
        #copy rest of the elements if any 
        while right < n:
            nums1[m] = nums2[right]
            m += 1
            right += 1    

        return nums1





        