# 🔐 Keylogger Detection Tool

A lightweight Python-based tool designed to detect potential keylogger activity on Windows systems. It monitors running processes and analyzes behavior to flag suspicious activity commonly associated with keyloggers.

## 🚀 Features
- Real-time monitoring of active processes
- Detection of suspicious keylogging behavior
- Generates logs and basic reports
- Simple CLI-based interface
- Works on Windows environments

## 🛠️ Technologies Used
- Python 3.x
- `psutil` for process monitoring
- `os` and `subprocess` modules for system-level interaction

## 🧠 Detection Logic
The tool applies basic behavioral heuristics to:
- Monitor processes accessing the keyboard too frequently
- Detect usage of Windows APIs often used by keyloggers
- Flag hidden or suspicious background processes

## 📦 Installation

```bash
git clone https://github.com/waaqaar/Keylogger-Detection-Tool.git
cd Keylogger-Detection-Tool
pip install -r requirements.txt
python detector.py
