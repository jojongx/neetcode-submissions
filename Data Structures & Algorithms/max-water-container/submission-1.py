class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        total = 0
        while left < right:
            min_height = min(heights[left], heights[right])
            total = max(total, (right - left) * min_height)
            if min_height == heights[left]:
                left += 1
            else:
                right -= 1

        return total
