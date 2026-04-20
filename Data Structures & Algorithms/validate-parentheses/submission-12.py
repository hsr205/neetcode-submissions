from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        if not s or len(s) == 1:
            return False

        stack:deque = deque()
        open_bracket_list:list = ["(", "[", "{"]
        closing_bracket_list:list = [")", "]", "}"]

        for character in s:

            if character in open_bracket_list:
                stack.append(character)

            if character in closing_bracket_list:
                
                if not stack:
                    return False

                current_element:str = stack[-1]

                if current_element == "(" and character == ")":
                    stack.pop()
                elif current_element == "[" and character == "]":
                    stack.pop()
                elif current_element == "{" and character == "}":
                    stack.pop()
                else:
                    return False

        is_stack_empty:bool = not stack

        return is_stack_empty
        