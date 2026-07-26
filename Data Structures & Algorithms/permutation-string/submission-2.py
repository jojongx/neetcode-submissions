class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l2 < l1:
            return False

        res = False
        master = defaultdict(int)
        for ch in s1:
            master[ch] += 1

        for i in range(l1, l2+1):
            curr = master.copy()
            print(s2[i-l1:i])
            for ch in s2[i-l1:i]:
                if ch not in curr:
                    break
                curr[ch] -= 1
                
            if not any(curr.values()):
                return True

        return res