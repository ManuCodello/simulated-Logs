<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>simulated-Logs | Log Simulation & Analysis</title>
  <style>
    body {
      font-family: 'Segoe UI', Roboto, sans-serif;
      background: linear-gradient(180deg, #f3f5f7 0%, #ffffff 100%);
      color: #2c3e50;
      margin: 0;
      padding: 0;
    }
    header {
      text-align: center;
      padding: 60px 20px 40px;
      background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
      color: #fff;
    }
    h1 {
      margin: 0;
      font-size: 2.8em;
      font-weight: 700;
    }
    h1 span {
      color: #4dd0e1;
    }
    .subtitle {
      font-size: 1.2em;
      opacity: 0.9;
      margin-top: 10px;
    }
    .badges {
      margin-top: 25px;
    }
    .badges img {
      margin: 5px;
      height: 28px;
    }
    main {
      max-width: 900px;
      margin: 40px auto;
      background: #fff;
      border-radius: 14px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
      padding: 40px;
      animation: fadeIn 0.8s ease;
    }
    h2 {
      border-left: 6px solid #4dd0e1;
      padding-left: 10px;
      color: #2c3e50;
      margin-top: 45px;
      font-size: 1.6em;
    }
    pre {
      background: #1e1e1e;
      color: #dcdcdc;
      padding: 14px;
      border-radius: 6px;
      overflow-x: auto;
      font-size: 0.95em;
    }
    code {
      font-family: Consolas, 'Courier New', monospace;
    }
    ul {
      line-height: 1.8;
    }
    li {
      margin-bottom: 4px;
    }
    footer {
      text-align: center;
      padding: 40px;
      color: #555;
      font-size: 0.9em;
      background-color: #f4f6f8;
      margin-top: 60px;
    }
    footer strong {
      color: #000;
    }
    a {
      color: #4dd0e1;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>

  <header>
    <h1>📄 <span>simulated-Logs</span></h1>
    <p class="subtitle"><strong>Log Simulation & Analysis Tool</strong></p>
    <div class="badges">
      <img src="https://img.shields.io/badge/Language-Python-3670a0?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
      <img src="https://img.shields.io/badge/Module-logging%20&%20simulation-orange?style=for-the-badge" alt="Module Badge">
      <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License Badge">
    </div>
  </header>

  <main>
    <section>
      <h2>📘 Overview</h2>
      <p>
        <strong>simulated-Logs</strong> is a complete Python project designed to
        <strong>generate, simulate, and analyze log data automatically</strong>.  
        Ideal for developers, data engineers, and DevOps professionals who need
        realistic logs for testing pipelines, monitoring, and machine learning experiments.
      </p>
    </section>

    <section>
      <h2>🧰 Key Features</h2>
      <ul>
        <li>🕵️ Generate realistic log entries with timestamps, identifiers, and severity levels (<code>INFO</code>, <code>WARN</code>, <code>ERROR</code>).</li>
        <li>🔄 Simulate live log streams to files or network targets.</li>
        <li>📊 Analyze log data and produce reports (counts, errors, frequencies).</li>
        <li>⚙️ Modular design — independent generator, simulator, and analyzer modules.</li>
        <li>💡 Fully customizable output format, rate, and structure.</li>
      </ul>
    </section>

    <section>
      <h2>📁 Project Structure</h2>
      <pre><code>simulated-Logs/
├── generator.py             # Builds structured synthetic log entries
├── simulator.py             # Emits log entries at a configurable rate
├── analyzer.py              # Parses logs and computes statistics
├── configs/                 # JSON configuration files
├── requirements.txt         # Dependencies list
└── README.html              # Project documentation
</code></pre>
    </section>

    <section>
      <h2>⚙️ Setup & Usage</h2>
      <h3>Installation</h3>
      <pre><code>git clone https://github.com/ManuCodello/simulated-Logs.git
cd simulated-Logs
pip install -r requirements.txt
</code></pre>

      <h3>Generate Logs</h3>
      <pre><code>python generator.py --config configs/logconfig.json
</code></pre>

      <h3>Simulate Logs</h3>
      <pre><code>python simulator.py --rate 100 --output logs/output.log
</code></pre>

      <h3>Analyze Logs</h3>
      <pre><code>python analyzer.py --input logs/output.log --report reports/summary.csv
</code></pre>
    </section>

    <section>
      <h2>🧠 How It Works</h2>
      <ol>
        <li><strong>generator.py</strong> → builds synthetic logs with metadata.</li>
        <li><strong>simulator.py</strong> → streams logs in real-time or writes them to a file.</li>
        <li><strong>analyzer.py</strong> → processes logs, computes stats, detects spikes or errors.</li>
      </ol>
    </section>

    <section>
      <h2>📊 Example Use Cases</h2>
      <ul>
        <li>Testing and benchmarking **log ingestion pipelines**.</li>
        <li>Creating **synthetic datasets** for SIEM or anomaly detection models.</li>
        <li>Teaching **data engineering** or **DevOps** monitoring workflows.</li>
      </ul>
    </section>

    <section>
      <h2>🚀 Future Enhancements</h2>
      <ul>
        <li>Integration with **Kafka**, **AWS Kinesis**, or WebSocket streaming.</li>
        <li>Support for **distributed simulation clusters**.</li>
        <li>Advanced analytics dashboards (e.g., Grafana or Streamlit).</li>
        <li>Web interface to control and visualize simulations.</li>
      </ul>
    </section>

    <section>
      <h2>👤 Author</h2>
      <p>
        <strong>Manu Codello</strong> — Computer Science Student at Universidad Nacional de Asunción.<br>
        Passionate about automation, data systems, and intelligent developer tools.
      </p>
    </section>

    <section>
      <h2>📜 License</h2>
      <p>This project is released under the <strong>MIT License</strong>.  
      Feel free to use, modify, and share with proper credit.</p>
    </section>
  </main>

  <footer>
    © 2025 <strong>Manu Codello</strong> — Crafted with precision, curiosity, and a love for clean code. ⚡
  </footer>

</body>
</html>

</html>

