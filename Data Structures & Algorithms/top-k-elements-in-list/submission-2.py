class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict_obj:dict[int,int] = {}

        for num in nums:
            if num not in dict_obj:
                dict_obj[num] = 1
            else:
                dict_obj[num] += 1

        sorted_dict:dict[int,int] = dict(sorted(dict_obj.items(), key=lambda item: item[1], reverse=True))

        result_list:list[int] = list(sorted_dict.keys())[0:k]

        return result_list
        