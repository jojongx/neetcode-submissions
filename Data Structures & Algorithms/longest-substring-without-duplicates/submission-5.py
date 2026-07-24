class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        curr = 0
        dupes = {}
        for i in range(0, len(s)):
            c = s[i]
            if c in dupes:
                curr = max(curr, dupes[c] + 1)
            maxLength = max(maxLength, i - curr + 1)
            dupes[c] = i
        return maxLength