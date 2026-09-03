class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            vals = self.timeMap[key]
            l = 0
            r = len(vals) - 1
            best = None
            while l <= r:
                m = (r + l) // 2
                if vals[m][0] == timestamp:
                    return vals[m][1]
                elif vals[m][0] > timestamp:
                    r = m - 1
                else:
                    best = vals[m][1]
                    l = m + 1
            if best is not None:
                return best
        
        return ""
                
        
