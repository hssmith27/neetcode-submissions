class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        current_tasks = []
        pending_tasks = []
        freq = defaultdict(int)

        for task in tasks:
            freq[task] += 1

        for key, value in freq.items():
            current_tasks.append([-value, key])

        heapq.heapify(current_tasks)

        cycles = 0
        while current_tasks or pending_tasks:
            print(pending_tasks, current_tasks)
            cycles += 1
            for pending_task in pending_tasks:
                if pending_task[1] == 0:
                    heapq.heappush(current_tasks, pending_task[0])
                    pending_tasks.remove(pending_task)
                pending_task[1] -= 1

            if current_tasks:
                current = heapq.heappop(current_tasks)
                print(current)
                current[0] += 1
                if current[0] < 0:
                    pending_tasks.insert(0, [current, n])
            print()

        return cycles

