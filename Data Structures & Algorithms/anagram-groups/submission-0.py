class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        for s in strs:
            if len(groups) == 0:
                groups.append([s])
                continue
            found = False
            for g in groups:
                if "".join(sorted(g[0])) == "".join(sorted(s)):
                    g.append(s)
                    found = True
                    break
            if not found:
                groups.append([s])
        return groups
