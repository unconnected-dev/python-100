#Crawler Log Folder
#https://leetcode.com/problems/crawler-log-folder/description/

caseLogs_1 = ["d1/","d2/","../","d21/","./"]
caseLogs_2 = ["d1/","d2/","./","d3/","../","d31/"]
caseLogs_3 = ["d1/","../","../","../"]
caseLogs_4 = ["./","../","./"]
caseLogs_5 = ["fl6/","nz1/","../","./"]
caseLogs_6 = ["./","../","./"]
caseLogs_7 = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]

if False:
    def winOperations(logs):
        stack = []
        
        for log in logs:
            if stack and log == "../":
                stack.pop()
            elif log == "./":
                continue
            elif log != "../":
                stack.append(log)
        
        res = 0
        if len(stack) > 1:
            res = len(stack)
        elif len(stack) == 1 and stack[0] != "./" and stack[0] != "../":
            res = 1
        
        return res

if False:
    def winOperations(logs):
        stack = []
        
        for log in logs:
            if log == "./":
                continue
            elif stack and log == "../":
                stack.pop()
            elif log != "../":
                stack.append(log)
                
        res = 0
        if len(stack) >= 1:
            res = len(stack)
        
        return res

if True:
    def winOperations(logs):
        stack = []
        
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(log)

        return len(stack)
        
print(f"{winOperations(caseLogs_1)}")
print(f"{winOperations(caseLogs_2)}")
print(f"{winOperations(caseLogs_3)}")
print(f"{winOperations(caseLogs_4)}")
print(f"{winOperations(caseLogs_5)}")
print(f"{winOperations(caseLogs_6)}")
print(f"{winOperations(caseLogs_7)}")