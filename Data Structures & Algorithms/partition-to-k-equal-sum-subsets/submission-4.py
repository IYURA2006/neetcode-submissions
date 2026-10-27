class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_numbers = sum(nums)
        if sum_numbers % k != 0:
            return False
        
        target_sum = sum_numbers // k #gettin integer
        visited = [False] * len(nums)
        nums.sort(reverse = True)

        def divide_subset(i, n_bucket_left, cur_sum):
            if n_bucket_left == 0:
                return True
            
            if cur_sum == target_sum:
                return divide_subset(0, n_bucket_left - 1, 0)

            for j in range(i, len(nums)):
                if visited[j] or nums[j] + cur_sum > target_sum:
                    continue
                
                visited[j] = True
                if divide_subset(j+1,n_bucket_left, cur_sum + nums[j]):
                    return True
                visited[j] = False
            
            return False
        return divide_subset(0, k, 0)



