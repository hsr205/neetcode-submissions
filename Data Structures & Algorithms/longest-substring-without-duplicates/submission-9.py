class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        if len(set(s)) == 1:
            return 1

        max_length:int = 0
        starting_index:int = 0
        ending_index:int = 1
        window_set:set = set()
        window_list:list[str] = []

        while ending_index <= len(s):
            
            window_list = s[starting_index : ending_index]
            window_set:set = set(window_list)

            if len(window_list) != len(window_set):
                starting_index += 1
                max_length = max(max_length, len(window_set))

            ending_index += 1
            
        max_length = max(max_length, len(window_set))

        return max_length
        