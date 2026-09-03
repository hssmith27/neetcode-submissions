class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = [] # (position, speed)

        for i in range(len(position)):
            cars.append(tuple([position[i], speed[i]]))
            
        cars = sorted(cars, key=lambda x : x[0], reverse=True)
        
        for position, speed in cars:
            time = (target - position) / speed
            if len(fleets) == 0 or fleets[-1] < time:
                fleets.append(time)

        return len(fleets)

            
