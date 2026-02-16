# 🔐 Mini SIEM Lab (Red + Blue Team Simulation)

A beginner-friendly **Security Information and Event Management (SIEM) lab** built using Python and Flask.
This project demonstrates how login attacks can be **detected, logged, monitored, and blocked** in a simulated environment.

---

## 📌 Project Overview

This lab simulates a real cybersecurity workflow:

Attacker → Target Server → Log Collection → SIEM Monitoring → Alert → Block

The goal is to understand how security systems detect brute-force attacks and generate alerts using log monitoring.

---

## ⚙️ Features

* Flask-based target server
* Brute-force attack simulation
* Real-time log monitoring
* IP blocking after repeated attempts
* Distributed attack detection
* Persistent blocklist storage
* Simple SIEM alert engine

---

## 🧠 Security Concepts Demonstrated

* SIEM fundamentals
* Intrusion Detection System (IDS)
* Intrusion Prevention System (IPS)
* Brute-force attack detection
* Log monitoring
* IP blocking
* Distributed attack awareness

---

## 🗂️ Project Structure

```
mini-siem-lab/
│
├── server.py        # Target server with detection logic
├── attacker.py      # Attack simulation script
├── siem.py          # Log monitoring (mini SIEM)
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Start the target server

```
python server.py
```

### 3. Start SIEM monitoring

```
python siem.py
```

### 4. Simulate attacker

```
python attacker.py
```

---

## 🔍 Example Detection Output

```
SIEM EVENT: Login attempt recorded
⚠️ ALERT: Blocking IP 127.0.0.1
SIEM ALERT: Blocked attacker detected!
```

---

## 📈 Future Improvements

* Dashboard visualization
* Time-window attack detection
* Multiple attacker simulation
* ELK / Wazuh integration
* Web interface for alerts

---

## 👨‍💻 Author

Vishnu Prathap

---

## 📚 Learning Purpose

This project was created as a **hands-on cybersecurity learning lab** to understand how SIEM pipelines work in practice.
