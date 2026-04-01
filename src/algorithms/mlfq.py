def schedule(processes, q1=2, q2=4, aging_threshold=10):
    n = len(processes)
    queues = [[], [], []]
    
    gantt = []
    time = 0
    completed = 0
    arrival_queue = sorted(processes, key=lambda p: p.arrival)

    def enqueue(proc, queue_level):
        proc.current_queue = queue_level
        queues[queue_level].append(proc)

    while completed < n:
        # 1. Arrival Logic
        arrived = [p for p in arrival_queue if p.arrival <= time]
        for p in arrived:
            enqueue(p, 0)
            arrival_queue.remove(p)

        # 2. Aging Logic
        for q_idx in [1, 2]:
            still_waiting = []
            for p in queues[q_idx]:
                p.age = getattr(p, 'age', 0) + 1
                if p.age >= aging_threshold:
                    p.age = 0
                    enqueue(p, q_idx - 1)
                else:
                    still_waiting.append(p)
            queues[q_idx] = still_waiting

        # 3. Selection Logic
        current_proc = None
        active_queue = None
        for q_idx in range(3):
            if queues[q_idx]:
                current_proc = queues[q_idx].pop(0)
                active_queue = q_idx
                break

        # 4. CPU Idle Logic
        if current_proc is None:
            if arrival_queue:
                gap = arrival_queue[0].arrival - time
                for _ in range(gap):
                    gantt.append("Idle")
                time = arrival_queue[0].arrival
            else:
                break
            continue

        # 5. Metrics
        if current_proc.start_time == -1:
            current_proc.start_time = time
            current_proc.response_time = time - current_proc.arrival

        # 6. Execution Slice
        if active_queue == 0:
            quantum = q1
        elif active_queue == 1:
            quantum = q2
        else:
            quantum = current_proc.remaining 

        exec_time = min(quantum, current_proc.remaining)
        
        # FIX: Append the PID as a string for every second of execution
        for _ in range(exec_time):
            gantt.append(str(current_proc.pid))
        
        time += exec_time
        current_proc.remaining -= exec_time
        current_proc.age = 0 

        # 7. Check arrivals during slice
        newly_arrived = [p for p in arrival_queue if p.arrival <= time]
        for p in newly_arrived:
            enqueue(p, 0)
            arrival_queue.remove(p)

        # 8. Completion/Demotion
        if current_proc.remaining == 0:
            current_proc.completion_time = time
            current_proc.turnaround_time = time - current_proc.arrival
            current_proc.waiting_time = current_proc.turnaround_time - current_proc.burst
            completed += 1
        else:
            next_level = min(active_queue + 1, 2)
            enqueue(current_proc, next_level)

    return gantt