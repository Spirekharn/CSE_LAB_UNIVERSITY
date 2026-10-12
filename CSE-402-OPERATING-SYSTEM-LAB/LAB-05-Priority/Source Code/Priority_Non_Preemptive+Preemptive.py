process = ["P1", "P2", "P3", "P4", "P5"]
at      = [3, 0, 2, 1, 4]
bt      = [4, 4, 3, 6, 2]
pr      = [2, 0, 1, 1, 3]

n = len(process)


def print_table(title, ct_list):
    total_tat = 0
    total_wt  = 0
    print(f"\n{title}")
    print("Process\tAT\tBT\tPR\tCT\tTAT\tWT")
    for i in range(n):
        tat = ct_list[i] - at[i]
        wt  = tat - bt[i]
        total_tat += tat
        total_wt  += wt
        print(f"{process[i]}\t{at[i]}\t{bt[i]}\t{pr[i]}\t{ct_list[i]}\t{tat}\t{wt}")
    print(f"Avg TAT = {total_tat / n:.2f}")
    print(f"Avg WT  = {total_wt  / n:.2f}")

ct   = [0] * n
done = [False] * n
time = 0
completed = 0

while completed < n:
    best = -1
    for i in range(n):
        if at[i] <= time and not done[i]:
            if best == -1 or pr[i] < pr[best] or (pr[i] == pr[best] and at[i] < at[best]):
                best = i

    if best == -1:
        time += 1
        continue

    time += bt[best]
    ct[best] = time
    done[best] = True
    completed += 1

print_table("Non-Preemptive Priority Scheduling", ct)

ct        = [0] * n
remaining = bt.copy()
time      = 0
completed = 0

while completed < n:
    best = -1
    for i in range(n):
        if at[i] <= time and remaining[i] > 0:
            if best == -1 or pr[i] < pr[best] or (pr[i] == pr[best] and at[i] < at[best]):
                best = i

    if best == -1:
        time += 1
        continue

    remaining[best] -= 1
    time += 1

    if remaining[best] == 0:
        ct[best] = time
        completed += 1

print_table("Preemptive Priority Scheduling", ct)

