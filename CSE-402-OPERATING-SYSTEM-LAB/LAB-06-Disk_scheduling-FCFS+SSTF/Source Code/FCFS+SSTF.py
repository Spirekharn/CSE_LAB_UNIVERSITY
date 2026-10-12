req  = [0, 30, 41, 62, 14, 20]
head = 20

req = [r for r in req if r != head]

print("Initial Head Position:", head)
print("Request Queue:", req)

# FCFS
total_fcfs = 0
cur = head
fcfs_seq = [head]

print("\nFCFS Total Seek Movements")
print("From\tTo\tSeek")
for r in req:
    seek = abs(r - cur)
    print(f"{cur}\t{r}\t{seek}")
    total_fcfs += seek
    cur = r
    fcfs_seq.append(r)

print("FCFS Total Seek =", total_fcfs)
print("Seek Sequence:", " -> ".join(map(str, fcfs_seq)))

# SSTF
remaining = req.copy()
total_sstf = 0
cur = head
sstf_seq = [head]

print("\nSSTF Total Seek Movements")
print("From\tTo\tSeek")
while remaining:
    closest = min(remaining, key=lambda x: abs(x - cur))
    seek = abs(closest - cur)
    print(f"{cur}\t{closest}\t{seek}")
    total_sstf += seek
    cur = closest
    sstf_seq.append(closest)
    remaining.remove(closest)

print("SSTF Total Seek =", total_sstf)
print("Seek Sequence:", " -> ".join(map(str, sstf_seq)))

# Comparison
print("\nComparison")
print("FCFS Total Seek =", total_fcfs)
print("SSTF Total Seek =", total_sstf)

if total_sstf < total_fcfs:
    print("SSTF is better less seek time")
elif total_fcfs < total_sstf:
    print("FCFS is better less seek time")
else:
    print("Both have equal seek time")

    