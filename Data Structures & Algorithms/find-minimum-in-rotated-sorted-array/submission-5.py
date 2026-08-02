class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right]:
            return res
        if len(nums) >= 2 and nums[-2] > nums[-1]:
            return nums[-1]

        while left < right:
            mid = left + (right - left) // 2

            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1
                res = nums[left]

        return res