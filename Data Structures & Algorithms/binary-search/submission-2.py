class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1

        return low if (low < len(nums) and nums[low] == target) else -1