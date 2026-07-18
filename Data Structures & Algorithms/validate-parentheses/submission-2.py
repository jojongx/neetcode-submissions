class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                match c:
                    case ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    case ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                    case '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
        if len(stack) == 0:
            return True
        return False