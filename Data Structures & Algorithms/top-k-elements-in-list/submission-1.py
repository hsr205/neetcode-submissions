class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_frequency_dict:dict[int, int] = {}

        for num in nums:
            if nums_frequency_dict.get(num) == None:
                nums_frequency_dict[num] = 1
            else:
                nums_frequency_dict[num] += 1

        sorted_dict:dict[int,int] = dict(sorted(nums_frequency_dict.items(), key=lambda item: item[1], reverse=True))
        
        index:int = 0
        result_list:list[int] = []


        for num, frequency in sorted_dict.items():
            
            if index == k:
                break
            
            result_list.append(num)

            index += 1

        return result_list

        