lst = [
    ["P0",3,5],
    ["p1",2,4],
    ["p2",4,3],
    ["p3",1,2],
    ["p4",5,3]
]
lst.sort(key=lambda x:x[1])
ct = []
tat = []
wt = []
current_time = 0
for i in lst:
    name, at, bt = i
    if current_time < at:
        current_time = at
    current_time += bt
    ct.append(current_time)
    turnaround = current_time - at
    tat.append(turnaround)
    waiting = turnaround - bt
    wt.append(waiting)
print(f"{'P_id':<6}{'AT':<6}{'BT':<6} {'CT':<6}{'TAT':<8}{'WT':<6}")
for i in range(len(lst)):
    print(f"{lst[i][0]:<6}{lst[i][1]:<6}{lst[i][2]:<6}{ct[i]:<6}{tat[i]:<8}{wt[i]:<6}")
avg_tat = sum(tat) / len(tat)
print(f"\nAverage TAT: {avg_tat:.2f}")
avg_wt = sum(wt) / len(wt)
print(f"Average WT:  {avg_wt:.2f}")





