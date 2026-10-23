class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        
        left_pointer:int = 1
        right_pointer:int = piles[-1]

        max_eating_speed:int = math.inf

        while left_pointer <= right_pointer:

            total_hours:int = 0
            middle_pointer:int = (left_pointer + right_pointer) // 2


            for num_bannanas in piles:

                hours_to_eat_banannas:int = math.ceil((num_bannanas / middle_pointer))
                total_hours += hours_to_eat_banannas

    
            if total_hours <= h:
                right_pointer = middle_pointer - 1
                max_eating_speed = min(max_eating_speed, middle_pointer)

            else:
                left_pointer = middle_pointer + 1


        return max_eating_speed
        