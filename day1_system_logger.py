import psutil
import platform
import datetime

print("=== Day 1: System Info Logger (April 11, 2026) ===")
print(f"Date & Time: {datetime.datetime.now()}")
print(f"OS: {platform.system()} {platform.release()}")
print(f"Python Version: {platform.python_version()}")

# Show CPU and Memory usage - links to Operating Systems concepts
print(f"\nCPU Usage: {psutil.cpu_percent(interval=1)}%")
print(f"Memory Usage: {psutil.virtual_memory().percent}%")

print("\n✅ Script completed! This links to OS module - processes and resource monitoring.")
