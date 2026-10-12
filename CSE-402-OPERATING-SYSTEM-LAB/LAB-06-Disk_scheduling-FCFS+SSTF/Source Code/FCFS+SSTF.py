req  = [0, 30, 41, 62, 14, 20]
head = 20

req = [r for r in req if r != head]

print("Initial Head Position:", head)
print("Request Queue:", req)

total_fcfs = 0
cur = head
fcfs_seq = [head]

print("\nFCFS Total Seek Movements")
print(f"{'From':<8}{'To':<8}{'Seek':<8}")
print("-" * 24)
for r in req:
    seek = abs(r - cur)
    print(f"{cur:<8}{r:<8}{seek:<8}")
    total_fcfs += seek
    cur = r
    fcfs_seq.append(r)

print("-" * 24)
print(f"{'FCFS Total Seek':<16} = {total_fcfs}")
print("Seek Sequence:", " -> ".join(map(str, fcfs_seq)))

remaining = req.copy()
total_sstf = 0
cur = head
sstf_seq = [head]

print("\nSSTF Total Seek Movements")
print(f"{'From':<8}{'To':<8}{'Seek':<8}")
print("-" * 24)
while remaining:
    closest = min(remaining, key=lambda x: abs(x - cur))
    seek = abs(closest - cur)
    print(f"{cur:<8}{closest:<8}{seek:<8}")
    total_sstf += seek
    cur = closest
    sstf_seq.append(closest)
    remaining.remove(closest)

print("-" * 24)
print(f"{'SSTF Total Seek':<16} = {total_sstf}")
print("Seek Sequence:", " -> ".join(map(str, sstf_seq)))

print("\nComparison")
print(f"{'FCFS Total Seek':<20} = {total_fcfs}")
print(f"{'SSTF Total Seek':<20} = {total_sstf}")

if total_sstf < total_fcfs:
    print("SSTF is better -- less seek time")
elif total_fcfs < total_sstf:
    print("FCFS is better -- less seek time")
else:
    print("Both have equal seek time")