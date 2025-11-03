class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)

        k = r

        while l <= r:
            speed = (l + r) // 2
            if speed == 0:
                break
                
            time = 0

            for i in piles:
                time += math.ceil(i / speed)
            if time <= h:
                k = min(k, speed)
                r = speed - 1
            else:
                l = speed + 1
        return k

