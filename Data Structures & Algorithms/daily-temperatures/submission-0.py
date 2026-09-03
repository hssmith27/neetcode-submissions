class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            current = temperatures[i]

            while len(stack) > 0 and current > stack[-1][0]:
                prev = stack.pop()
                result[prev[1]] = i - prev[1]
            
            stack.append([current, i])

        print(stack)
        return result