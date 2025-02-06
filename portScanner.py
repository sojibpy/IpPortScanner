import socket
import time


def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)  # Faster scanning
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                print(f"Port {port} is OPEN")
                open_ports.append(port)

            sock.close()
        except KeyboardInterrupt:
            print("Scan interrupted by user.")
            break
        except socket.error:
            print(f"Couldn't connect to {target_ip}")
            break

    return open_ports


def suggest_security_measures(ports):
    suggestions = {
        22: "Port 22 (SSH) is open. Disable root login and use key-based authentication.",
        80: "Port 80 (HTTP) is open. Ensure a secure HTTPS setup.",
        443: "Port 443 (HTTPS) is open. Regularly update your SSL certificates.",
        3306: "Port 3306 (MySQL) is open. Restrict access to specific IP addresses.",
        3389: "Port 3389 (RDP) is open. Limit remote access or use VPN."
    }

    print("\nSecurity Suggestions:")
    for port in ports:
        if port in suggestions:
            print(f" - {suggestions[port]}")


# Main Execution
target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

open_ports = scan_ports(target_ip, start_port, end_port)
if open_ports:
    print("\nOpen Ports Found:", open_ports)
    suggest_security_measures(open_ports)
else:
    print("No open ports found.")
