class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum = 0
        stack = []
        for op in operations :
            stack.append(op)
            if op == "+" :
                stack.pop()
                temp = int(stack[-1])
                stack.pop()
                res = temp + int(stack[-1])
                stack.append(temp)
                stack.append(res)
            elif op == "D" :
                stack.pop()
                res = 2 * int(stack[-1])
                stack.append(res)
            elif op == "C" :
                stack.pop()
                stack.pop()
        print(stack)
        while len(stack) > 0 :
            sum += int(stack[-1])
            stack.pop()
        return sum