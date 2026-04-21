class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        total_boats:int = 0
        left_pointer:int = 0
        right_pointer:int = len(people) - 1
        
        people.sort()

        while left_pointer < right_pointer:


            left_num:int = people[left_pointer]
            right_num:int = people[right_pointer]


            sum_value:int = left_num + right_num

            if sum_value <= limit:
                total_boats += 1
                left_pointer += 1
                right_pointer -= 1

            elif right_num <= limit:
                total_boats += 1
                right_pointer -= 1

        if left_pointer == right_pointer:
            total_boats += 1
                    

        return total_boats

        