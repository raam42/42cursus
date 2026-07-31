#!/bin/bash

# Architecture
arch=$(uname -a)

# CPU Physical
cpuv=$(grep "physical id" /proc/cpuinfo | sort -u | wc -l)

# vCPU
cpuc=$(nproc)

# Memory Usage
mem_used=$(free -m | awk 'NR==2{print $3}')
mem_total=$(free -m | awk 'NR==2{print $2}')
mem_rate=$(free -m | awk 'NR==2{printf "%.2f%%", $3/$2*100}')

# Disk Usage
disk_used=$(df -m | grep "^/dev/" | grep -v "/boot" | awk '{use += $3} END {print use}')
disk_total=$(df -m | grep "^/dev/" | grep -v "/boot" | awk '{tot += $2} END {print tot}')
disk_rate=$(df -m | grep "^/dev/" | grep -v "/boot" | awk '{use += $3; tot += $2} END {printf "%.2f%%", use/tot*100}')

# CPU Load
cpu_load=$(top -bn1 | grep "^%Cpu" | awk '{printf "%.1f%%", 100 - $8}')

# Last Boot
lb=$(who -b | awk '{print $3 " " $4}')

# LVM Use
lvm_use=$(if [ $(lsblk | grep "lvm" | wc -l) -gt 0 ]; then echo yes; else echo no; fi)

# TCP Connections
tcp_conn=$(ss -ta state established | wc -l)

# Active Users
users_log=$(users | wc -w)

# IP and MAC
ip=$(hostname -I)
mac=$(ip link | grep "link/ether" | awk '{print $2}')

# Sudo Commands
sudo_cmd=$(journalctl _COMM=sudo -q | grep COMMAND | wc -l)

wall "    # Architecture: $arch
    # CPU physical: $cpuv
    # vCPU: $cpuc
    # Memory Usage: $mem_used/${mem_total}MB ($mem_rate)
    # Disk Usage: ${disk_used}/${disk_total}Mb ($disk_rate)
    # CPU load: $cpu_load
    # Last boot: $lb
    # LVM use: $lvm_use
    # Connections TCP : $tcp_conn ESTABLISHED
    # User log: $users_log
    # Network: IP $ip ($mac)
    # Sudo : $sudo_cmd cmd"