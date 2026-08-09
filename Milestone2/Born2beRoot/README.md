# Born2beRoot

> **Project Status:** Completed & Hardened  
> **Evaluated OS:** Debian 12 (Bookworm) / Debian 13  
> **Virtualization:** VirtualBox  

---

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture & Specifications](#system-architecture--specifications)
3. [Security & Network Configuration](#security--network-configuration)
4. [Evaluation Defense Guide (Q&A)](#evaluation-defense-guide-qa)

---

## 🛠️ Project Overview
**Born2beRoot** is an introduction to system administration and virtualization. The goal of this project is to set up your first secure virtual machine following strict structural and security rules, utilizing LVM partitioning, a secure firewall, a custom password policy, and a functional web server setup (with WordPress for the bonus).

---

## 💻 System Architecture & Specifications

### 🗄️ LVM (Logical Volume Manager) Structure
The system uses LVM to organize partitions flexibly, separating critical mount points to prevent disk overflow and isolate system logs/data:
* **`root (/)`**: Main system partition.
* **`swap`**: Virtual memory allocation.
* **`home`**: User data and configurations.
* **`srv`**: Data for services (like WordPress/web server files).
* **`var`**: System logs, package caches, and variable files.
* **`var/log`**: Dedicated partition for logs to prevent log-flooding attacks from crashing the core system.

### 🔒 Security & Monitoring Implementations
* **Password Policy:** Enforced via `libpam-pwquality` (minimum length, uppercase/lowercase, numbers, no consecutive repeating characters, and username checks).
* **Firewall (UFW):** Configured to block all incoming traffic by default and only allow specific necessary ports (such as SSH on port `4242` and HTTP/HTTPS if applicable).
* **AppArmor:** Active Linux kernel security module restricting application capabilities.
* **Monitoring Script (`monitoring.sh`):** A custom bash script running every 10 minutes via cron that broadcasts vital system metrics (uptime, CPU load, disk/memory usage, active connections, LVM status, etc.) to all terminals.

---

## 🧠 Evaluation Defense Guide (Q&A)

This section contains the core theoretical answers required during your Born2beRoot defense:

### 1. What is a Virtual Machine?
It is software that simulates a computer system and can execute programs as if it were a real computer. It allows you to create multiple simulated environments or dedicated resources from a single physical hardware system.

### 2. Why did you choose Debian?
This is a personal choice; in my opinion, the subject itself explains that it is simpler to do in Debian, and if you look for documentation/tutorials, there are many and almost all of them have been done in Debian.

### 3. Core Differences: Debian vs. Rocky Linux
| Aspect | Debian | Rocky Linux |
| :--- | :--- | :--- |
| **Base** | Independent | RHEL |
| **Package Manager** | APT (`.deb`) | DNF (`.rpm`) |
| **Stability** | Flexible | Very stable (enterprise) |
| **Lifecycle / Support** | 3-5 years | 10 years |
| **Typical Use** | General | Enterprise servers |

> **Summary:** Debian is more versatile and community-driven. Rocky is a robust, enterprise-grade option with long-term support.

### 4. What is the purpose of Virtual Machines?
Its goal is to provide an execution environment independent of the hardware platform and operating system, which conceals the details of the underlying platform and allows a program to run consistently on any platform.

### 5. Differences between `apt` and `aptitude`
Aptitude is an enhanced version of apt. APT is a lower-level package manager and aptitude is a higher-level package manager. Another major difference is the functionality they offer. Aptitude provides better functionality compared to apt-get. Both are capable of providing the means necessary to perform package management. However, if a feature-rich approach is desired, it should be Aptitude.

### 6. What is AppArmor?
It is a Linux kernel security module that allows the system administrator to restrict the capabilities of a program.

### 7. What is LVM?
It is a logical volume manager. It provides a method to allocate space on mass storage devices that is more flexible than conventional partitioning schemes for storing volumes.
