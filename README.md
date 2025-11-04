# 📄 simulated-Logs

> **Log Simulation & Analysis Tool**

<div align="center">

![Python](https://img.shields.io/badge/Language-Python-3670a0?style=for-the-badge&logo=python&logoColor=white)
![Logging & Simulation](https://img.shields.io/badge/Module-logging%20&%20simulation-orange?style=for-the-badge)
![License MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📘 Overview

**simulated-Logs** is a project built to **generate, simulate, and analyze system logs** automatically.  
It allows developers, analysts, and engineers to **produce synthetic log data** for testing, monitoring, and AI training scenarios.  

This tool is ideal for:
- Testing log ingestion pipelines.
- Validating monitoring and alerting systems.
- Building training datasets for log analysis and anomaly detection.

---

## 🧰 Key Features

- 🕵️ Generate **realistic synthetic logs** with timestamps, identifiers, and levels (`INFO`, `WARN`, `ERROR`).
- 🔄 Simulate **continuous log streams** for applications, servers, or services.
- 📊 **Analyze logs** automatically — count levels, detect patterns, summarize statistics.
- ⚙️ **Modular architecture**: generation, simulation, and analytics modules.
- 💡 Fully **customizable** — define format, volume, and rate.

---

## 📁 Project Structure

```bash
simulated-Logs/
├── generator.py             # Core logic to build synthetic log entries
├── simulator.py             # Engine to feed logs into files or streams
├── analyzer.py              # Processes logs and compiles metrics
├── configs/                 # Configuration files for format and rate
├── requirements.txt         # Python dependencies
└── README.md                # This document
```
⚙️ Setup & Usage
🔹 Installation
```
bash

git clone https://github.com/ManuCodello/simulated-Logs.git
cd simulated-Logs
pip install -r requirements.txt
```
🔹 Generate Logs
```
bash

python generator.py --config configs/logconfig.json
```
🔹 Run Simulation
```
bash

python simulator.py --rate 100 --output logs/output.log
```
🔹 Analyze Logs
```
bash

python analyzer.py --input logs/output.log --report reports/summary.csv
```
🧠 How It Works
generator.py — builds structured log entries (timestamp, level, service, message).

simulator.py — emits log entries at a configurable rate (to files or streams).

analyzer.py — parses log files and computes metrics (error rates, counts per level, anomalies).

📊 Use Cases
🧩 Load testing for logging pipelines

🔐 Building synthetic SIEM or monitoring datasets

🧠 Training AI/ML models for anomaly or pattern detection

🧪 Teaching & practicing data engineering / DevOps skills

🧾 Future Enhancements
Integration with Kafka, AWS Kinesis, or Socket servers

Support for distributed simulation clusters

Add visual dashboards for real-time log visualization

Develop web UI for controlling log streams

👤 Author
Manu Codello
📍 Computer Science Student — Universidad Nacional de Asunción
💡 Passionate about automation, data engineering & developer tools.
