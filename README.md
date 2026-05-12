# 🛜 Basic Network Sniffer

A Python-based Network Packet Sniffer developed using Scapy for capturing and analyzing live network traffic.

This project captures packets in real time and displays useful information such as:

- Source IP Address
- Destination IP Address
- Protocol Type
- Packet Length
- Payload Preview

The tool works similarly to a lightweight command-line version of Wireshark and helps understand how network communication happens.

---

# 🚀 Features

✅ Live Packet Capturing  
✅ Protocol Detection (TCP / UDP / ICMP)  
✅ Real-Time Traffic Monitoring  
✅ Packet Length Analysis  
✅ Payload Preview  
✅ Colorful Terminal Output  
✅ Windows Compatible using Npcap  
✅ Interface Selection Support  

---

# 🛠️ Technologies Used

- Python
- Scapy
- Colorama
- Npcap

---

# 📂 Project Structure

```bash
CodeAlpha_NetworkSniffer/
│
├── sniffer.py
├── requirements.txt
├── README.md
├── screenshots/
└── logs/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/CodeAlpha_NetworkSniffer.git
```

---

## 2️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Install Npcap (For Windows)

Download and install Npcap:

https://npcap.com/#download

While installing:
✔ Enable **WinPcap Compatibility Mode**

---

# ▶️ Running the Project

Run the Python script:

```bash
py sniffer.py
```

Select the network interface when prompted.

Example:

```bash
Wi-Fi
```

The sniffer will start capturing packets in real time.

---

# 📸 Screenshots

## Interface Selection
(Add Screenshot Here)

## Packet Capture Output
(Add Screenshot Here)

## Live Traffic Monitoring
(Add Screenshot Here)

---

# 📊 Example Output

```text
No    Time        Source IP          Destination IP      Proto   Length
--------------------------------------------------------------------------------
1     13:44:37    20.44.10.123       10.24.117.249      TCP     54
2     13:44:37    10.24.117.249      20.44.10.123       UDP     175
```

---

# 🎯 Learning Outcomes

- Understanding packet structure
- Network protocol analysis
- Real-time packet monitoring
- Working with Scapy library
- Basics of cybersecurity and traffic analysis

---

# 🔮 Future Improvements

- GUI Dashboard
- Packet Filtering
- Suspicious Traffic Detection
- CSV Export
- DNS & HTTP Monitoring
- Live Graph Visualization

---

# 📌 Internship Task

This project was developed as part of the CodeAlpha Cyber Security Internship Task.

---

# 👨‍💻 Author

R Lasya Amrutha 
