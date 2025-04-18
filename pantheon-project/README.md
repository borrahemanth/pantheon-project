# pantheon-project
# Pantheon Congestion Control Evaluation – CS Assignment

This repository contains the experiments, logs, and analysis scripts for evaluating three congestion control algorithms using [Pantheon](https://github.com/StanfordSNR/pantheon) and [Mahimahi](https://github.com/ravinet/mahimahi). This was done for Programming Assignment 3 in Computer Networks (Spring 2025).

## 🧪 Experiment Summary

- **Protocols compared:**  
  - CUBIC  
  - BBR  
  - Copa

- **Test durations:** 60 seconds per run
- **Network environments simulated:**  
  1. **Low-latency / High-bandwidth:** 50 Mbps, 10 ms RTT  
  2. **High-latency / Low-bandwidth:** 1 Mbps, 200 ms RTT

- **Metrics collected:**  
  - Throughput over time  
  - RTT statistics (average, 95th percentile)  
  - Packet loss rate  

---

## ⚙️ Setup Instructions

### 1. Clone and Install Pantheon
```bash
git clone https://github.com/StanfordSNR/pantheon.git
cd pantheon
git submodule update --init --recursive
