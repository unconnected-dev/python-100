#Min Stack
#https://leetcode.com/problems/min-stack/description/

if False:
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_value = None
            self.min_value_stack = []

        def push(self, val: int) -> None:
            if self.min_value == None or self.min_value > val:
                self.min_value = val
            
            self.min_value_stack.append(self.min_value)
            self.stack.append(val)

        def pop(self) -> None:
            self.min_value_stack.pop()
            self.stack.pop()
                            
            if len(self.min_value_stack) == 0:
                self.min_value = None
            else:
                self.min_value = self.min_value_stack[-1]

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min_value
        
if False:
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
        
if True:
    class MinStack:

        def __init__(self):
            self.stack = []
            self.min_value_stack = []

        def push(self, val: int) -> None:
            min_val = min(val, self.min_value_stack[-1]) if self.min_value_stack else val
                
            self.min_value_stack.append(min_val)
            self.stack.append(val)

        def pop(self) -> None:
            self.min_value_stack.pop()
            self.stack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min_value_stack[-1]