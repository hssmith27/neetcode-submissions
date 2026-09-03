class TimeMap:
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        left = 0
        right = len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                res = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return res
        
