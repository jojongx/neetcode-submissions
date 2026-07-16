class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        temp, res = [], []
        for num, count in freq.items():
            temp.append([count, num])
        temp.sort()
        while len(res) < k:
            res.append(temp.pop()[1])
        return res