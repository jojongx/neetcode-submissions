class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            d = target-nums[i]
            if nums[i] in diffs:
                return [diffs[nums[i]], i]
            diffs[d] = i