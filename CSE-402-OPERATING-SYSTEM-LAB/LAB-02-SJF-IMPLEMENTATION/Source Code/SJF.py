#shortest_job_first (non-preemptive)
process = ["P1", "P2", "P3", "P4", "P5"]
at = [2, 3, 0, 1, 1]
bt = [5, 1, 2, 3, 6]

n = len(process)
ct = [0] * n
wt = [0] * n
tat = [0] * n
done = [0] * n

time = 0
completed = 0

while completed < n:
    x = -1
    for i in range(n):
        if at[i] <= time and done[i] == 0:
            if x == -1 or bt[i] < bt[x]:
                x = i

    if x == -1:
        time += 1
    else:
        time += bt[x]
        ct[x] = time
        done[x] = 1
        completed += 1

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

sjf_avg_tat = sum(tat) / n
sjf_avg_wt = sum(wt) / n


def print_table(title, headers, rows):
    col_w = 10
    print(f"\n {title} ")
    print("".join(f"{h:^{col_w}}" for h in headers))
    for row in rows:
        print("".join(f"{str(v):^{col_w}}" for v in row))


sjf_rows = [[process[i], at[i], bt[i], ct[i], tat[i], wt[i]] for i in range(n)]
print_table(" SJF", ["Process", "AT", "BT", "CT", "TAT", "WT"], sjf_rows)
print(f"\nAverage TAT = {sjf_avg_tat:.2f}")
print(f"Average WT = {sjf_avg_wt:.2f}")


lst = [
    ["P1", 3, 5],
    ["P2", 2, 4],
    ["P3", 4, 3],
    ["P4", 1, 2],
    ["P5", 5, 3]
]

lst.sort(key=lambda x: x[1])

ct2 = []
tat2 = []
wt2 = []
time = 0

for name, arr, burst in lst:
    if time < arr:
        time = arr
    time += burst
    ct2.append(time)
    turnaround = time - arr
    tat2.append(turnaround)
    wt2.append(turnaround - burst)

avg_tat = sum(tat2) / len(tat2)
avg_wt = sum(wt2) / len(wt2)

fcfs_rows = [[lst[i][0], lst[i][1], lst[i][2], ct2[i], tat2[i], wt2[i]] for i in range(len(lst))]
print_table("FCFS", ["P_id", "AT", "BT", "CT", "TAT", "WT"], fcfs_rows)
print(f"\nAverage TAT = {avg_tat:.2f}")
print(f"Average WT = {avg_wt:.2f}")


print("\n\nCOMPARISON")
print("SJF is better in terms of TAT than FCFS" if sjf_avg_tat < avg_tat
      else "FCFS is better in terms of TAT than SJF")
print("SJF is better in terms of WT than FCFS" if sjf_avg_wt < avg_wt
      else "FCFS is better in terms of WT than SJF")
