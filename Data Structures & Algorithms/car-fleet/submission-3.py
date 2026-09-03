class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))   
        pairs.sort(key=lambda x: x[0], reverse=True)
        stack = []

        for p, s in pairs:
            time = (target - p) / s
            if not stack:
                stack.append(time)
            elif stack[-1] < time:
                stack.append(time)

        return len(stack)
