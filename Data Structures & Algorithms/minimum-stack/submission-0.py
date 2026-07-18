class MinStack:

    def __init__(self):
        self.stack = []
        self.my_dict = defaultdict(int)
        self.min_val = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_val = val
        elif val < self.min_val:
            self.min_val = val
        self.stack.append(val)
        self.my_dict[len(self.stack)-1] = self.min_val

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0:
            self.min_val = None
        else:
            self.min_val = self.my_dict[len(self.stack)-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.my_dict[len(self.stack)-1]
