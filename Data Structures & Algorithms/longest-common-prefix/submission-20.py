class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        result_str:str = ""
        word_1:str = strs[0]
        min_str_length:int = len(min(strs))

        for index in range(0, len(word_1)):

            word_1_chr:str = word_1[index]

            is_same_chr:bool = False

            for word_2 in strs[1:]:

                if index >= min_str_length:
                    break

                word_2_chr:str = word_2[index]

                is_same_chr = word_1_chr == word_2_chr

                if is_same_chr is False:
                    break

            if is_same_chr:
                result_str += word_1_chr
            else:
                break


        return result_str
        