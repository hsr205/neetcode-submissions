from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack:deque[int] = deque()

        for op in operations:

            if op.isnumeric() or "-" in op:
                if "-" in op:
                    negative_value:int = int(op.replace("-", "")) * -1
                    stack.append(negative_value)
                else:
                    stack.append(int(op))
            
            elif op == "+":
                addition_result:int = int(stack[-2]) + int(stack[-1])
                stack.append(addition_result)

            elif op == "C":
                stack.pop()
            
            elif op == "D":
                multiplication_result:int = int(stack[-1]) * 2
                stack.append(multiplication_result)

        

        return sum(stack)
        