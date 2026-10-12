from collections import deque

process = ["P1", "P2", "P3", "P4", "P5"]
at      = [3, 0, 2, 1, 4]
bt      = [4, 4, 3, 6, 2]
pr      = [2, 0, 1, 1, 3]

N = len(process)


def table(title, ct):
    tat = [ct[i] - at[i] for i in range(N)]
    wt  = [tat[i] - bt[i] for i in range(N)]

    print(f"\n{title}")
    print(f"{'Process':<10}{'AT':<6}{'BT':<6}{'PR':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")
    for i in range(N):
        print(f"{process[i]:<10}{at[i]:<6}{bt[i]:<6}{pr[i]:<6}{ct[i]:<6}{tat[i]:<6}{wt[i]:<6}")
    print(f"Avg TAT = {sum(tat)/N:.2f}")
    print(f"Avg WT  = {sum(wt)/N:.2f}")


def priority(tq):
    rem    = bt.copy()
    ct     = [0] * N
    q      = {p: deque() for p in sorted(set(pr))}
    added  = set()
    time   = 0
    done   = 0

    while done < N:
        for i in range(N):
            if i not in added and at[i] <= time:
                q[pr[i]].append(i)
                added.add(i)

        if not any(q.values()):
            time += 1
            continue

        p = min(k for k in q if q[k])
        i = q[p].popleft()

        run = min(tq, rem[i])
        for _ in range(run):
            rem[i] -= 1
            time += 1
            for j in range(N):
                if j not in added and at[j] <= time:
                    q[pr[j]].append(j)
                    added.add(j)

        if rem[i] == 0:
            ct[i] = time
            done += 1
        else:
            q[p].append(i)

    table(f"Priority Scheduling (Lower # = Higher Priority) | TQ = {tq}", ct)


priority(1)
priority(2)
priority(3)


