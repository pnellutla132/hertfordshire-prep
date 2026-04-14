import random
import time

print("port scanner simulator")

ports= {22: "SSH", 21: "FTP", 23: "Telnet", 80: "HTTP", 443: "HTTPS"}

target= "192.168.1.1"

is_open=random.choice([True, False])


open_ports= {}

for port, service in ports.items():
    print(f"Scanning port {port} ({service})...")
    time.sleep(1)  # Simulate scanning delay
    
    if is_open:
        print(f"Port {port} is OPEN - Service: {service}")
        open_ports.append((port, service))
    else:
        print(f"Port {port} is CLOSED - Service: {service}  ")

print("\n=== Scan completed ===")

if open_ports:
    print("\n⚠️  Security Alert - Open Ports Found:")
    for port, service in open_ports:
        print(f"   • Port {port} ({service}) - Consider closing if not needed")
        
    if 23 in [p[0] for p in open_ports]:
        print("   🔥 CRITICAL: Telnet is open - Very insecure!")
    if 3389 in [p[0] for p in open_ports]:
        print("   🔥 CRITICAL: RDP is open - High risk of brute force attacks!")
else:
    print("✅ No open ports found - Good security posture!")

print("\nThis is a simulation. Real port scanners are used in penetration testing.")
