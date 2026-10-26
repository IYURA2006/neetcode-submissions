class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [9,1,4,2,3,3,7]
        #[  4  4,  3,3,  2 ,2,1]
        
        # [0, 3, 1, 3, 2, 3]
        # [4  3  3  2  2  1]   
        longest_from_point = [1] * len(nums)

        i = len(nums) - 2
        n = len(nums)
        longest_subSeq = 0

        while i >= 0:
            cur_longest_seq = 1
            for x in range(i, n):
                if nums[i] < nums[x]:
                    cur_longest_seq = max(cur_longest_seq, longest_from_point[x] + 1)
            longest_from_point[i] = cur_longest_seq
            i -=1

        print(longest_from_point)
        return max(longest_from_point)
