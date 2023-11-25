from sys import stdin
def main():
    cases = int(stdin.readline().strip())
    for _ in range(cases):
        n, m = map(int, input().split())
        jobs = list(map(int, input().split()))
        queue = [(priority, idx) for idx, priority in enumerate(jobs)]
        max_list = sorted(jobs, reverse=True)
        time = 0
        while queue:
            job = queue.pop(0)
            if job[0] == max_list[0]:
                time += 1
                max_list.pop(0)
                if job[1] == m:
                    print(time)
                    break
            else:
                queue.append(job)
main()
