class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = []
        dupes = set()
        for i in range(1, len(nums)-1):
            low = 0
            high = len(nums) - 1
            while (low < high):
                if (low == i):
                    low += 1
                elif (high == i):
                    high -= 1
                else:
                    total = nums[low] + nums[high] + nums[i]
                    if total < 0:
                        low += 1
                    elif total > 0:
                        high -= 1
                    elif total == 0:
                        vals = tuple(sorted((nums[low], nums[high], nums[i])))
                        if vals not in dupes:
                            dupes.add(vals)
                            trips.append([vals[0], vals[1], vals[2]])
                        low += 1
        return trips