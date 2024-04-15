#Min Stack
#https://leetcode.com/problems/min-stack/description/

if True:
    class MinStack:

        def __init__(self):
            self.stack = []
            self.min_value_stack = [float('inf')]

        def push(self, val: int) -> None:
            min_val = min(val, self.min_value_stack[-1])
            self.min_value_stack.append(min_val)
            self.stack.append(val)

        def pop(self) -> None:
            self.min_value_stack.pop()
            self.stack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min_value_stack[-1]