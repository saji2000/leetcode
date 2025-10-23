class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleet = 0
        ahead_t = 0.0

        for pos, speed in cars:
            
            time = (target - pos)/speed

            if ahead_t < time:
                fleet += 1
                ahead_t = time


        return fleet
                