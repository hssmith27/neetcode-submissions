class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) != 0 and stack[-1][1] < temperatures[i]:
                prev_index = stack[-1][0]
                result[prev_index] = i - prev_index
                stack.pop()
            stack.append((i, temperatures[i]))

        return result