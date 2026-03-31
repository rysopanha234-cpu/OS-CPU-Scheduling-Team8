def calculate_metrics(processes):
    total_wt = total_tat = total_rt = 0
    n = len(processes)

    print("\nProcess\tWT\tTAT\tRT")

    for p in processes:
        tat = p.completion_time - p.arrival
        wt = tat - p.burst
        rt = p.response_time

        total_wt += wt
        total_tat += tat
        total_rt += rt

        print(f"{p.pid}\t{wt}\t{tat}\t{rt}")

    print(f"\nAverage WT: {total_wt / n:.2f}")
    print(f"Average TAT: {total_tat / n:.2f}")
    print(f"Average RT: {total_rt / n:.2f}")