#!/bin/bash

# Disk Usage Monitor
THRESHOLD=80
USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//')
if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "Disk usage is high: $USAGE%" >> system.log
fi

# CPU and Memory Usage
echo "CPU Usage: $(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')%" >> system.log
echo "Memory Usage: $(free -m | awk '/Mem:/ {printf "%.2f", $3/$2*100}')%" >> system.log

# Backup Files
BACKUP_DIR="backup_$(date +%Y%m%d)"
mkdir -p "$BACKUP_DIR"
cp *.txt "$BACKUP_DIR" 2>/dev/null
echo "Backup completed at $(date)" >> system.log
