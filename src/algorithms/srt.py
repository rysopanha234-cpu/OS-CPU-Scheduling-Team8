from process import Process
from utils.gantt import print_gantt
from utils.metrics import calculate_metrics

# =========================
# SRT Algorithm
# =========================

def srt(processes):
    time = 0
    completed = 0
    n = len(processes)
    gantt = []

    # Run until all processes are completed
    while completed < n:
        
        # Get all processes that have arrived and are not finished
        ready = [p for p in processes if p.arrival <= time and p.remaining > 0]
        
        # If no process is ready, CPU is idle
        if not ready:
            gantt.append("Idle")  # Record idle time
            time += 1             # Move time forward
            continue              # Skip to next iteration

        # Select process with shortest remaining time (SRT logic)
        current = min(ready, key=lambda x: x.remaining)

        # If this is the first time the process is executed
        if current.response_time == -1:
            # Response time = first start time - arrival time
            current.response_time = time - current.arrival

        # Execute the selected process for 1 time unit
        gantt.append(current.pid)  # Add process ID to Gantt chart
        current.remaining -= 1     # Reduce remaining time
        time += 1                 # Increment current time

        # If process finishes execution
        if current.remaining == 0:
            current.completion_time = time  # Record completion time
            completed += 1                 # Increase completed count

    # Return the Gantt chart (execution timeline)
    return gantt
