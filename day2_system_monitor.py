import psutil
import platform
import datetime
import time

def get_system_stats():
    """Return current system statistics"""
    return {
        'cpu': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }

print("=== Day 2: Enhanced System Monitor (April 12, 2026) ===")
print(f"Date & Time: {datetime.datetime.now()}")
print(f"OS: {platform.system()} {platform.release()}")
print(f"Python Version: {platform.python_version()}\n")

print("Starting 20-second system monitoring...\n")

for i in range(10):                  # 10 snapshots
    votkai = get_system_stats()      # ← Using votkai as you want
    
    print(f"Snapshot {i+1} at {datetime.datetime.now().strftime('%H:%M:%S')}:")
    print(f"   CPU Usage     : {votkai['cpu']}%")
    print(f"   Memory Usage  : {votkai['memory']}%")
    print(f"   Disk Usage    : {votkai['disk']}%")
    
    # Warnings
    if votkai['cpu'] > 80:
        print("   ⚠️  HIGH CPU USAGE - Possible performance issue!")
    elif votkai['cpu'] > 50:
        print("   High CPU usage detected")
        
    if votkai['memory'] > 85:
        print("   ⚠️  HIGH MEMORY USAGE - System may slow down!")
    elif votkai['memory'] > 45:
        print("   High memory usage detected")
        
    if votkai['disk'] > 90:
        print("   ⚠️  DISK ALMOST FULL!")
    elif votkai['disk'] > 50:
        print("   DISK Almost Full! Consider cleaning up some space.")
    
    print("-" * 50)
    time.sleep(2)

# Save results to a file
with open("system_monitor_log.txt", "a") as file:
    file.write(f"\n=== Log at {datetime.datetime.now()} ===\n")
    file.write(f"CPU: {votkai['cpu']}%, Memory: {votkai['memory']}%, Disk: {votkai['disk']}%\n")
    file.write("-" * 40 + "\n")

print("\n✅ Monitoring completed!")
print("Results also saved to system_monitor_log.txt")
print("This script demonstrates process/resource monitoring — key OS concept!")