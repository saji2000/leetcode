class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleet = 0
        prev_t = 0.0

        for pos, speed in cars:
            time = (target - pos) / speed
            if prev_t < time:
                fleet += 1
                prev_t = time
        return fleet
