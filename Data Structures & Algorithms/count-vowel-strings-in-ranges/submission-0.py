class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        num_strs:int = 0
        left_pointer:int = 0
        result_list:list[int] = []
        vowel_list:list[str] = ['a', 'e', 'i', 'o', 'u']

        for start_index, end_index in queries:

            for index in range(start_index, end_index + 1):

                right_pointer:int = len(words[index]) - 1

                is_left_char_vowel:str = words[index][left_pointer] in vowel_list
                is_right_char_vowel:str = words[index][right_pointer] in vowel_list

                if is_left_char_vowel and is_right_char_vowel:
                    num_strs += 1

            result_list.append(num_strs)
            num_strs = 0


        return result_list
        