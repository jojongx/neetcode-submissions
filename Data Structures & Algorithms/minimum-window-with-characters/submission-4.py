class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_dict, win_dict = {}, {}
        for c in t:
            t_dict[c] = 1 + t_dict.get(c, 0)
        
        have, need = 0, len(t_dict)
        res, min_len = [-1, -1], float("infinity")
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            win_dict[c] = 1 + win_dict.get(c, 0)

            if c in t_dict and t_dict[c] == win_dict[c]:
                have += 1

            while have == need:
                if (r - l + 1) < min_len:
                    res = [l, r]
                    min_len = r - l + 1
                
                win_dict[s[l]] -= 1
                if s[l] in t_dict and win_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res

        return s[l:r+1] if min_len != float("infinity") else ""
