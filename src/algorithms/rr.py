from collections import deque
from process import Process
from utils.gantt import print_gantt
from utils.metrics import calculate_metrics

# =========================
# Round Robin Algorithm
# =========================
def round_robin(processes, quantum):
    queue = deque()   # Ready queue for RR (FIFO structure)
    time = 0
    gantt = []

    processes.sort(key=lambda x: x.arrival)  # Sort by arrival time
    i = 0

    while queue or i < len(processes):

        # Add newly arrived processes to the ready queue
        while i < len(processes) and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        # If no process is ready, CPU stays idle
        if not queue:
            gantt.append("Idle")
            time += 1
            continue

        # RR LOGIC: pick the first process in the queue (FIFO order)
        current = queue.popleft()

        # RR LOGIC: set response time only the first time process gets CPU
        if current.response_time == -1:
            current.response_time = time - current.arrival

        # RR LOGIC: process runs for a fixed time slice (quantum)
        # or until it finishes, whichever comes first
        run_time = min(quantum, current.remaining)

        # RR LOGIC: execute process for 'run_time' units
        for _ in range(run_time):
            gantt.append(current.pid)
            time += 1
            current.remaining -= 1

            # RR LOGIC: during execution, newly arrived processes
            # are added to the end of the queue (fair scheduling)
            while i < len(processes) and processes[i].arrival <= time:
                queue.append(processes[i])
                i += 1

        # RR LOGIC: if process is not finished after quantum,
        # put it back at the end of the queue (preemption)
        if current.remaining > 0:
            queue.append(current)
        else:
            # If finished, record completion time
            current.completion_time = time

    return gantt
