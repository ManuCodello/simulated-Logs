<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>simulated-Logs</title>
  <style>
    body { font-family: Arial, sans-serif; background-color: #f9f9f9; color: #333; margin: 0; padding: 20px; }
    header { text-align: center; padding: 40px 0; }
    h1 { margin: 0; font-size: 2.5em; color: #2c3e50; }
    .badges img { margin: 0 6px; vertical-align: middle; }
    .content { max-width: 900px; margin: auto; background: #fff; border-radius: 8px; padding: 30px; box-shadow: 0 0 12px rgba(0,0,0,0.06); }
    h2 { color: #34495e; margin-top: 40px; }
    pre { background: #272c30; color: #f8f8f2; padding: 15px; border-radius: 5px; overflow-x: auto; }
    code { font-family: Consolas, ‘Courier New’, monospace; color: #f8f8f2; }
    ul { list-style-type: square; }
    footer { text-align: center; font-size: 0.9em; color: #888; margin-top: 60px; }
  </style>
</head>
<body>

  <header>
    <h1>📄 simulated-Logs</h1>
    <p><strong>Log Simulation & Analysis Tool</strong></p>
    <div class="badges">
      <img src="https://img.shields.io/badge/Language-Python-3670a0?style=for-the-badge&logo=python&logoColor=white" alt="Python">
      <img src="https://img.shields.io/badge/Module-logging%20&%20simulation-orange?style=for-the-badge" alt="Logging & Simulation">
      <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
    </div>
  </header>

  <div class="content">

    <h2>📘 Overview</h2>
    <p>
      <strong>simulated-Logs</strong> is a comprehensive project designed to create, simulate, and analyze system logs automatically.  
      It helps developers, analysts, and security-oriented engineers generate synthetic log data, handle log workflows, and feed it into downstream systems—ideal for testing, monitoring, or training.
    </p>

    <h2>🧰 Key Features</h2>
    <ul>
      <li>🕵️ Generate realistic synthetic log entries with timestamps, identifiers, levels (INFO/WARN/ERROR).</li>
      <li>🔄 Simulate log streams for applications, servers or services (e.g., saving to files, sending over channels).</li>
      <li>📊 Analyze log output: count levels, detect patterns, prepare for ingestion.</li>
      <li>⚙️ Modular code architecture: separate generation, simulation, and analytics components.</li>
      <li>💡 Easily customizable: choose formats, volumes, simulation rate, output channels.</li>
    </ul>

    <h2>📁 Project Structure</h2>
    <pre><code>simulated-Logs/
├── generator.py             # Core logic to build synthetic log entries  
├── simulator.py             # Engine to feed logs into files or streams  
├── analyzer.py              # Processes logs, compiles stats and reports  
├── configs/                 # Configuration files for formats/rate/output  
├── requirements.txt         # Python dependencies  
└── README.html              # This document  
</code></pre>

    <h2>⚙️ Setup & Usage</h2>
    <h3>Installation</h3>
    <pre><code>git clone https://github.com/ManuCodello/simulated-Logs.git
cd simulated-Logs
pip install -r requirements.txt
</code></pre>

    <h3>Running Log Generation</h3>
    <pre><code>python generator.py --config configs/logconfig.json
</code></pre>

    <h3>Running Simulation</h3>
    <pre><code>python simulator.py --rate 100 --output logs/output.log
</code></pre>

    <h3>Analysis & Reporting</h3>
    <pre><code>python analyzer.py --input logs/output.log --report reports/summary.csv
</code></pre>

    <h2>🧠 How It Works</h2>
    <p>
      1. <strong>generator.py</strong> builds structured log entries (timestamp, level, service, message) based on patterns.  
      2. <strong>simulator.py</strong> emits these entries at configurable rates, either into files or streaming targets.  
      3. <strong>analyzer.py</strong> ingests log files, parses entries, and computes useful metrics (counts per level, rate over time, error spikes).  
    </p>

    <h2>📊 Highlights & Use Cases</h2>
    <p>
      - Useful for <strong>load testing</strong> logging pipelines.  
      - Great for training DevOps/SME teams in parsing and monitoring log data.  
      - Helps build <strong>SIEM test datasets</strong> or verify alerting rules.  
    </p>

    <h2>🧾 Future Enhancements</h2>
    <ul>
      <li>Integrate real-time streaming into Kafka or AWS Kinesis.</li>
      <li>Support large-scale log volumes and distributed simulation clusters.</li>
      <li>Advanced analytics: anomaly detection, log correlation and visualization dashboards.</li>
      <li>Add UI web interface for simulation control and monitoring.</li>
    </ul>

    <h2>👤 Author</h2>
    <p>
      <strong>Manu Codello</strong> — Computer Science Student, Universidad Nacional de Asunción<br>
      Focused on automation, data engineering, and developer tools.
    </p>

    <h2>📜 License</h2>
    <p>This project is released under the <strong>MIT License</strong>. You are free to use, modify, and distribute with attribution.</p>

  </div>

  <footer>
    © 2025 Manu Codello
  </footer>

</body>
</html>
