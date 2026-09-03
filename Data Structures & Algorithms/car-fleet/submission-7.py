class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs, cars = [], []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        pairs.sort(reverse=True)
        for pair in pairs:
            cars.append((target - pair[0])/pair[1])

        index = 1
        while index < len(cars):
            if cars[index] <= cars[index - 1]:
                cars.pop(index)
            else:
                index += 1

        return len(cars)