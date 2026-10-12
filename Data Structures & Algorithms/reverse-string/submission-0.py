class Solution:
    def reverseString(self, s: List[str]) -> None:

        if not s or len(s) == 1:
            return

        front_pointer:int = 0
        back_pointer:int = len(s) - 1

        while front_pointer < back_pointer:
            
            front_str:str = s[front_pointer]
            back_str:str = s[back_pointer]
            temp_str:str = front_str


            s[front_pointer] = back_str
            s[back_pointer] = temp_str

            front_pointer += 1
            back_pointer -= 1



        