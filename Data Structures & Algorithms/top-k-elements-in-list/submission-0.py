class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        res = []
        for i in range(k):
            max_pair = (-1001, -1001)
            for key in freq:
                if freq[key] > max_pair[1]:
                    max_pair = (key, freq[key])
            res.append(max_pair[0])
            del freq[max_pair[0]]
        return res