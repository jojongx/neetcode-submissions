class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                curr = height[left]
                leftMax = max(leftMax, curr)
                total += leftMax - curr
            else:
                right -= 1
                curr = height[right]
                rightMax = max(rightMax, curr)
                total += rightMax - curr

        return total