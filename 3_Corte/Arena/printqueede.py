from collections import deque
from heapq import heapify, heappop

def print_job_time(test_cases):
    for _ in range(test_cases):
        n, m = map(int, input().split())
        jobs = list(map(int, input().split()))
        queue = deque([(priority, idx) for idx, priority in enumerate(jobs)])
        max_heap = [-priority for priority in jobs]
        heapify(max_heap)
        time = 0
        while queue:
            job = queue.popleft()
            if job[0] == -max_heap[0]:
                time += 1
                heappop(max_heap)
                if job[1] == m:
                    print(time)
                    break
            else:
                queue.append(job)
print_job_time(3)