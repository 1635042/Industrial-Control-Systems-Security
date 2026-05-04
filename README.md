# Industrial Control Systems Security (OpenPLC / SCADA)

## Description

This project analyzes the security of an Industrial Control System (ICS) in an OT environment using OpenPLC and ScadaBR.

The system simulates a water heater process where:

* OpenPLC acts as the PLC executing control logic
* ScadaBR acts as the HMI/SCADA for monitoring and control

The objective is to identify vulnerabilities in the communication between PLC and HMI and evaluate their impact.

---

## Architecture

* PLC (OpenPLC): Level 1 – Control layer
* SCADA/HMI (ScadaBR): Level 3 – Supervisory layer

The communication between both components is based on Modbus/TCP (port 502), which does not provide authentication or encryption.

The SCADA is considered the lower trust component due to its exposure and interaction with users.

---

## Attacks Implemented

### 1. Man-in-the-Middle (MitM)

* Traffic between PLC and HMI is intercepted
* Passive analysis using Wireshark
* Active attack implemented using a Python proxy
* Packets are modified before being forwarded

Result: Demonstrates lack of integrity protection in Modbus/TCP communication.

---

### 2. False Data Injection (FDI)

* Crafted Modbus packets are sent directly to the PLC
* Holding registers (e.g. setpoint) are modified
* Changes are reflected in the system without detection by the HMI

Result: System integrity is compromised without user awareness.

---

### 3. Denial of Service (DoS)

#### PLC DoS

* Multiple TCP connections are opened against port 502
* Communication resources are exhausted
* PLC becomes slow or unresponsive

#### HMI DoS

* HTTP requests are flooded against port 9090
* Server resources are exhausted
* HMI becomes unavailable (HTTP errors / freeze)

Result: Loss of availability in both PLC and HMI.

---

## Files

```id="files1"
attack_task2.py      # MitM attack
attack_task3.py      # False Data Injection
attack_dos_plc.py    # DoS attack on PLC
attack_dos_hmi.py    # DoS attack on HMI
Assignment 3.pdf     # Report with explanation and proof of concept
```

---

## Conclusion

The system is vulnerable due to:

* Lack of encryption and authentication in Modbus/TCP
* Weak trust boundary between PLC and SCADA
* Exposure to network-based attacks

These issues allow attackers to intercept, manipulate and disrupt industrial processes.

---

## Disclaimer

This project is for academic purposes only.
