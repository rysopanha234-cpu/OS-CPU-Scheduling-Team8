import matplotlib.pyplot as plt

def print_gantt(gantt_list):
    """Prints the text-based chart to the terminal."""
    if not gantt_list:
        print("Gantt Chart is empty.")
        return
    print("Gantt Chart:")
    print(" | ".join(gantt_list))

def save_visual_gantt(gantt_list, filename="gantt_chart.png"):
    """Generates a professional colorful chart using Matplotlib."""
    if not gantt_list:
        return

    # Using '_' for unused 'fig' to avoid the grey-out in VS Code
    _, ax = plt.subplots(figsize=(12, 3))
    
    # Each item in gantt_list is 1 second of time
    for i, pid in enumerate(gantt_list):
        # We use str(pid) so numbers and "Idle" both work
        ax.barh(str(pid), 1, left=i, color='skyblue', edgecolor='black', alpha=0.8)
    
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Process ID")
    ax.set_title("CPU Scheduling Gantt Chart")
    ax.grid(axis='x', linestyle='--', alpha=0.6)
    
    # Makes the chart look cleaner
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"--- Visual Gantt Chart saved as {filename} ---")