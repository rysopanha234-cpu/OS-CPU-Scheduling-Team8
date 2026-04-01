from process import Process
from utils.gantt import print_gantt, save_visual_gantt
from utils.metrics import calculate_metrics

# Import algorithms
from algorithms import fcfs, sjf, srt, rr, mlfq

def reset_processes(processes):
    for p in processes:
        p.remaining = p.burst
        p.start_time = -1
        p.completion_time = 0
        p.response_time = -1
        if hasattr(p, 'age'):
            p.age = 0

def get_user_input():
    procs = []
    try:
        n = int(input("Enter number of processes: "))
        for i in range(n):
            pid = input(f"Enter PID for Process {i+1}: ")
            arrival = int(input(f"  Arrival time for {pid}: "))
            burst = int(input(f"  Burst time for {pid}: "))
            procs.append(Process(pid, arrival, burst))
        return procs
    except ValueError:
        print("Error: Please enter numbers for Arrival and Burst times.")
        return None

if __name__ == "__main__":
    print("=== CPU Scheduling Simulator (Team 8) ===")
    
    processes = get_user_input()
    
    if processes:
        while True:
            print("\nSelect an Algorithm to Run:")
            print("1. FCFS (First Come, First Served)")
            print("2. SJF (Shortest Job First)")
            print("3. SRT (Shortest Remaining Time)")
            print("4. RR (Round Robin)")
            print("5. MLFQ (Multilevel Feedback Queue)")
            print("6. Exit")
            
            choice = input("\nEnter choice (1-6): ")

            if choice == '1':
                # Member A Placeholder
                print("\n--- Running FCFS (Coming Soon) ---")
                # gantt = fcfs.schedule(processes)
                # print_gantt(gantt)
                # save_visual_gantt(gantt, "fcfs_gantt.png")
                # calculate_metrics(processes)
                pass 

            elif choice == '2':
                # Member A Placeholder
                print("\n--- Running SJF (Coming Soon) ---")
                # gantt = sjf.schedule(processes)
                # print_gantt(gantt)
                # save_visual_gantt(gantt, "sjf_gantt.png")
                # calculate_metrics(processes)
                pass

            elif choice == '3':
                print("\n--- Running SRT ---")
                gantt = srt.srt(processes)
                print_gantt(gantt)
                save_visual_gantt(gantt, "srt_gantt.png")
                calculate_metrics(processes)
                reset_processes(processes)

            elif choice == '4':
                q = int(input("Enter Time Quantum for RR: "))
                print(f"\n--- Running RR (q={q}) ---")
                gantt = rr.round_robin(processes, q)
                print_gantt(gantt)
                save_visual_gantt(gantt, "rr_gantt.png")
                calculate_metrics(processes)
                reset_processes(processes)

            elif choice == '5':
                q1 = int(input("Enter Quantum for Q1: "))
                q2 = int(input("Enter Quantum for Q2: "))
                age = int(input("Enter Aging Threshold: "))
                print(f"\n--- Running MLFQ ---")
                gantt = mlfq.schedule(processes, q1, q2, age)
                print_gantt(gantt)
                save_visual_gantt(gantt, "mlfq_gantt.png")
                calculate_metrics(processes)
                reset_processes(processes)

            elif choice == '6':
                print("Exiting Simulator. Good luck with the project!")
                break
            
            else:
                print("Invalid choice. Please select 1-6.")