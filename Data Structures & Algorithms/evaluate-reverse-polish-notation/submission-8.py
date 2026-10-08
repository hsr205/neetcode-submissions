import math
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack:deque[int] = deque()

        result_value:int = 0

        for token in tokens:

            if token == "+":
                addition_value:int = stack[-2] + stack[-1]
                del stack[-2]
                del stack[-1]
                stack.append(addition_value)

            elif token == "-":
                sutraction_value:int = stack[-2] - stack[-1]
                del stack[-2]
                del stack[-1]
                stack.append(sutraction_value)
            
            elif token == "*":
                print(f"stack = {stack}")
                multiplication_value:int = stack[-2] * stack[-1]
                del stack[-2]
                del stack[-1]
                stack.append(multiplication_value)

            elif token == "/":
                division_value:int = stack[-2] / stack[-1]

                if division_value < 0:
                    division_value = math.ceil(division_value)
                
                elif division_value > 0:
                    division_value = math.floor(division_value)

                del stack[-2]
                del stack[-1]
                stack.append(int(division_value))

            elif token.isnumeric() or "-" in token:
                if "-" in token:
                    negative_token:int = int(token.replace("-", "")) * -1
                    stack.append(int(negative_token))
                else:
                    stack.append(int(token))

        return stack[0]
        