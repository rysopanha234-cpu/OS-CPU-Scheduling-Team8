import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

    while completed < n:
        ready = [p for p in processes if p.arrival <= time and p.remaining > 0]

        if not ready:
            gantt.append("Idle")
            time += 1
            continue

        current = min(ready, key=lambda x: x.remaining)

        if current.response_time == -1:
            current.response_time = time - current.arrival

        gantt.append(current.pid)
        current.remaining -= 1
        time += 1

        if current.remaining == 0:
            current.completion_time = time
            completed += 1

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

    print("===== SRT Scheduling =====")
    gantt = srt(processes)

    print("Gantt Chart:")
    print_gantt(gantt)

    calculate_metrics(processes)