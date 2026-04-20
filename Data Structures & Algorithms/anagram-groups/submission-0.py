class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 1 or len(strs) == 1 and strs[0] == "":
            return [[strs[0]]]

        tuple_dict:dict[tuple[list[int]], list[str]] = {}
        
        for str_element in strs:
            ascii_values_list:list[int] = []
            for character in str_element:
                ascii_values_list.append(ord(character))
            
            sorted_ascii_values_tuple:tuple[list[int]] = tuple(sorted(ascii_values_list))

            if tuple_dict.get(sorted_ascii_values_tuple) is None:
                tuple_dict[sorted_ascii_values_tuple] = [str_element]
            elif tuple_dict.get(sorted_ascii_values_tuple) is not None:
                tuple_dict[sorted_ascii_values_tuple].append(str_element)

        result_list:list[list[str]] = list(tuple_dict.values())

        return result_list
        