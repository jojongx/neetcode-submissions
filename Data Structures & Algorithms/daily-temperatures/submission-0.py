class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                day = stack.pop()[0]
                res[day] = i - day
            stack.append((i, temp))
        return res


        # res = []
        # stack = []
        # curr_high = 0
        # for i, temp in enumerate(temperatures):
        #     if temperatures[i] > curr_high:
        #         cnt = 1
        #         while stack:
        #             res[stack[-1]] = cnt
        #             cnt += 1
        #             stack.pop()
        #         curr_high = temp
        #     res.append(0)
        #     stack.append(i)
        
        return res