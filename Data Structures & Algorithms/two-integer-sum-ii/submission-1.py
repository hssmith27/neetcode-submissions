class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        values = {}
        index = 1

        while index <= len(numbers):
            values[index] = target - numbers[index - 1]
            for i in range(1, index):
                if numbers[index - 1] == values[i]:
                    return [i, index]
            index += 1
        return [-1, -1]