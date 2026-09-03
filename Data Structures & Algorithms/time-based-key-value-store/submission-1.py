class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key] += [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        values = [(0, "")] + self.time_map[key]

        while len(values) > 1:
            l, r = 0, len(values) - 1
            m = (r + l) // 2 + 1
            if values[m][0] == timestamp:
                return values[m][1]
            if values[m][0] < timestamp:
                values = values[m:]
            else:
                values = values[:m]

        return values[-1][1]
