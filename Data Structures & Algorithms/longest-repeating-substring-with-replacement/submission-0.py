class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        chars = set(s)

        for c in chars:
            cnt = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    cnt += 1
                while (r - l + 1) - cnt > k:
                    if s[l] == c:
                        cnt -= 1
                    l += 1
                max_len = max(max_len, r - l + 1)
        
        return max_len