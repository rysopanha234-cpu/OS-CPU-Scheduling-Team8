import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collections import deque
from process import Process
from utils.gantt import print_gantt
from utils.metrics import calculate_metrics

# =========================
# Round Robin Algorithm
# =========================
def round_robin(processes, quantum):
    queue = deque()
    time = 0
    gantt = []

    processes.sort(key=lambda x: x.arrival)
    i = 0

    while queue or i < len(processes):
        while i < len(processes) and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            gantt.append("Idle")
            time += 1
            continue

        current = queue.popleft()

        if current.response_time == -1:
            current.response_time = time - current.arrival

        run_time = min(quantum, current.remaining)

        for _ in range(run_time):
            gantt.append(current.pid)
            time += 1
            current.remaining -= 1

            while i < len(processes) and processes[i].arrival <= time:
                queue.append(processes[i])
                i += 1

        if current.remaining > 0:
            queue.append(current)
        else:
            current.completion_time = time

    return gantt

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
    ]

    quantum = int(input("Enter Time Quantum: "))

    print("\n===== Round Robin Scheduling =====")
    gantt = round_robin(processes, quantum)

    print("Gantt Chart:")
    print_gantt(gantt)

    calculate_metrics(processes)