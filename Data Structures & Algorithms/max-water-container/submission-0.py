class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        leftMaxHeight = 0
        rightMaxHeight = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            curArea = min(heights[left], heights[right]) * (right - left)
            maxWater = max(maxWater, curArea)
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        
        return maxWater

        