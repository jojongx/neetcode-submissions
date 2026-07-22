class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        length = len(height)
        rev = False
        
        i = 0
        while i < length:
            left = height[i]
            if left == 0:
                i += 1
                continue
            extra = 0
            for j in range(i + 1, length):
                right = height[j]
                if left <= right:
                    total += left * (j - i - 1) - extra
                    i = j - 1
                    break
                else:
                    extra += right
                    if j == length - 1 and height[j - 1] < right:
                        rev = True
                        k = i - 1
                        i = j - 1
            i += 1

        if rev:
            i = length - 1
            while i > k:
                right = height[i]
                if right == 0:
                    i -= 1
                    continue
                extra = 0
                for j in range(i - 1, k, -1):
                    left = height[j]
                    if right <= left:
                        total += right * (i - j - 1) - extra
                        i = j + 1
                        break
                    else:
                        extra += left
                i -= 1

        return total