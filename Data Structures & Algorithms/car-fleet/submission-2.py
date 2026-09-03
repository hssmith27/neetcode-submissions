class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ordered = []

        for i in range(len(position)):
            ordered.append([position[i], speed[i]])

        ordered.sort(key = lambda x : x[0])
        print(ordered)

        for i in range(len(ordered) - 1, -1, -1):
            car = ordered[i]
            position = car[0]
            speed = car[1]
            time = (target - position) / speed
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)