class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        length = len(heights)
        i, j = 0, 0

        for i in range(length):
            for j in range(length):
                tempArea = min(heights[i], heights[j]) * (j - i)
                if tempArea > maxArea:
                    maxArea = tempArea

        return maxArea