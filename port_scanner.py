
import socket


target = input("Enter the IP address or website (e.g., google.com): ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

print(f"\n🔍 Scanning ports {start_port} to {end_port} on {target}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Wait 0.5 seconds max for a response
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"✅ Port {port} is OPEN")
    sock.close()

print("\n✅ Scan complete!")
