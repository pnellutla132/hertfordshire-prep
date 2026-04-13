import time
import random

print("=== Day 4: Process State Simulator (Based on OSTEP Reading) ===\n")

processes = ["Chrome", "VS Code", "Python Script", "Discord", "Antivirus"]

# Track how many times each process was running
running_count = {proc: 0 for proc in processes}

for i in range(8):          # Simulate 8 time steps
    print(f"Time step {i+1}:")
    
    for proc in processes:
        state = random.choice(["Ready", "Running", "Blocked"])
        
        if state == "Running":
            print(f"  → {proc} is RUNNING on CPU")
            print(f"     OS scheduled {proc} to run")
            running_count[proc] += 1
        elif state == "Blocked":
            print(f"  → {proc} is BLOCKED (waiting for I/O)")
        else:
            print(f"  → {proc} is READY (waiting for CPU)")
    
    print("-" * 60)
    time.sleep(1.5)

# Final summary
print("\n=== Summary after simulation ===")
for proc, count in running_count.items():
    print(f"{proc} was running {count} times")

print("\nThis simulator shows how the OS manages process states (Ready → Running → Blocked)")