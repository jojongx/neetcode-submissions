class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for w in range(k, len(nums) + 1):
            high = float('-inf')
            for i in range(w-k, w):
                high = max(high, nums[i])
            res.append(high)
        
        return res