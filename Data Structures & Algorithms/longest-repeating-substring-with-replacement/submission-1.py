class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        count = {}

        maxf = l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # when window size - highest char freq > k,
            # reduce count of chars leaving window and move said window
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len