from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_dict:dict[str, list] = defaultdict(list)

        for word in strs:
            result_dict[''.join(sorted(word))].append(word)

        return list(result_dict.values())
        