class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1

        if target < nums[0] or nums[0] == nums[left]:
            right = len(nums) - 1
        else:
            right = left
            left = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1