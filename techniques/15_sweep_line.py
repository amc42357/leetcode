def sweep_line(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    
    events.sort(key=lambda x: (x[0], x[1]))
    
    count = 0
    max_count = 0
    for time, delta in events:
        count += delta
        max_count = max(max_count, count)
    
    return max_count

# Ejemplo: Meeting Rooms II (LeetCode 253)