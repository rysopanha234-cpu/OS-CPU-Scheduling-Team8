from process import Process
from utils.gantt import print_gantt
from utils.metrics import calculate_metrics

# import algorithms
from algorithms import fcfs, sjf, srt, rr, mlfq

def reset_processes(processes):
    for p in processes:
        p.remaining = p.burst
        p.start_time = -1
        p.completion_time = 0
        p.response_time = -1

if __name__ == "__main__":
    processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
    ]
    quantum = 2

    # Member A algorithms (placeholders)
    # gantt = fcfs.schedule(processes)
    # print_gantt(gantt)
    # calculate_metrics(processes)
    # reset_processes(processes)

    # gantt = sjf.schedule(processes)
    # print_gantt(gantt)
    # calculate_metrics(processes)
    # reset_processes(processes)

    # Member B algorithms
    print("\n===== SRT Scheduling =====")
    gantt = srt.srt(processes)
    print_gantt(gantt)
    calculate_metrics(processes)
    reset_processes(processes)

    print("\n===== RR Scheduling =====")
    gantt = rr.round_robin(processes, quantum)
    print_gantt(gantt)
    calculate_metrics(processes)
    reset_processes(processes)

    # Member C algorithm (placeholder)
    # gantt = mlfq.schedule(processes)
    # print_gantt(gantt)
    # calculate_metrics(processes)