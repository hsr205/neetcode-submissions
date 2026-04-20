from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False

        if len(s) == 1:
            return False

        stack:deque[str] = deque()

        for character in s:
            
            if character == "[" or character == "(" or character == "{":
                stack.append(character)

            if character == "]":
                if not stack:
                    return False
                top_item = stack[-1]

                if top_item == "[":
                    stack.pop()
                else:
                    return False

            elif character == ")":
                if not stack:
                    return False
                top_item = stack[-1]

                if top_item == "(":
                    stack.pop()
                else:
                    return False

            elif character == "}":
                if not stack:
                    return False
                top_item = stack[-1]

                if top_item == "{":
                    stack.pop()
                else:
                    return False

        return not stack
        