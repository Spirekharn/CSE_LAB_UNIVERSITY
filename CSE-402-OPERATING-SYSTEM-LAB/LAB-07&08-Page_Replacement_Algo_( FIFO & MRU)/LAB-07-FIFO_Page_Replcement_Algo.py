def fifo(pages, frame_size):
    frames = []
    hits = 0
    faults = 0
    insert_seq = []
    replace_seq = []
    print(f"Reference String : {pages}")
    print(f"Frame Size : {frame_size}")
    print(f"Page | Frames | Result")
    for page in pages:
        if page in frames:
            hits += 1
            result = "HIT"
        else:
            faults += 1
            result = "FAULT"
            insert_seq.append(page)

            if len(frames) < frame_size:
                frames.append(page)
            else:
                removed = frames.pop(0)
                replace_seq.append(f"{removed} {page}")
                frames.append(page)
        print(f" {page} | {str(frames):<10} | {result}")
    total = len(pages)
    print(f"Hits : {hits}")
    print(f"Faults : {faults}")
    print(f"Hit Ratio : {hits}/{total} = {hits/total:.2f}")
    print(f"Fault Ratio : {faults}/{total} = {faults/total:.2f}")
    print(f"Insert seq : {insert_seq}")
    print(f"Replace seq : {replace_seq}")
pages = [1, 2, 3, 4, 5, 1, 2, 3, 1]
frame_size = 3
fifo(pages, frame_size)