Cloud Linux Monitor 

A lightweight Linux system monitoring service written in Python and designed to run as a background service using systemd.

I buil;t this project to practice , linux,python and DevOps concepts. 
EC2 environment.

What this project Does.
* Monitors system-level metrics (CPU, memory, disk, etc.)
* runs continuously as a Linux service
* Writes logs to a single log file
* Designed to be simple, reliable, and low-resource

Technologogies used 
- Python 3
- Linux (Ubuntu)
- systemd
- Virtual Environment (venv)
- EC2 (AWS Free Tier)


project Structure/

cloud-linux-monitor/

* src/
   - config
     - __init__.py
     - settings.py
   - main.py
   - core/
         - __init__.py
         - cpu.py
         - memory.py
         - disk.py
         - netowrk.py
    - utils
        - __init__.py
        - config.py
        - logger.py
       
* logs/
  - monitor.log
* scripts
* systemd/
   -cloud-monitor.server 
* test
   - gitignore
   - README.md
   - requirements.txt

****** Very important ************

How to works ?

systemd
  ↓
Python service (main.py)
  ↓
System metrics collected
  ↓
Logs written to logs/monitor.log


how to run ?

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m src.main

how to run as a linux service ?

sudo cp systemd/cloud-monitor.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable cloud-monitor
sudo systemctl start cloud-monitor

Check status ?

sudo systemctl status cloud-monitor
