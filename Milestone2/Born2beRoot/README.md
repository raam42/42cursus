*This project has been created as part of the 42 curriculum by rodrigoa.*

# Born2beRoot

> **Project Status:** Completed & Hardened  
> **Evaluated OS:** Debian 12 (Bookworm)  
> **Virtualization:** VirtualBox  

---

## 📋 Table of Contents
1. [Description](#1-description)
   * [Project Goal & Overview](#project-goal--overview)
   * [Operating System Choice (Debian vs. Rocky)](#operating-system-choice-debian-vs-rocky)
   * [Main Design Choices](#main-design-choices)
2. [Comparative Technical Analysis](#2-comparative-technical-analysis)
   * [Debian vs. Rocky Linux](#debian-vs-rocky-linux)
   * [AppArmor vs. SELinux](#apparmor-vs-selinux)
   * [UFW vs. firewalld](#ufw-vs-firewalld)
   * [VirtualBox vs. UTM](#virtualbox-vs-utm)
3. [Instructions](#3-instructions)
   * [Running the Virtual Machine](#running-the-virtual-machine)
   * [SSH Connection](#ssh-connection)
   * [Monitoring Script Verification](#monitoring-script-verification)
4. [Resources & AI Usage](#4-resources--ai-usage)

---

## 1. Description

### Project Goal & Overview
**Born2beRoot** is an introduction to system administration, virtualization, and system security. The primary objective is to create a secure, hardened virtual machine following strict administrative guidelines, enforcing rigid password rules, partitioning with LVM, implementing a firewall, managing users and groups, and setting up system monitoring.

---

### Operating System Choice (Debian vs. Rocky)
For this project, **Debian** was chosen as the operating system.
* **Advantages of Debian:** Excellent community support, extensive documentation for the 42 curriculum, lightweight package management via APT, and renowned stability.
* **Disadvantages of Debian:** Stable releases can feature slightly older software packages compared to rolling-release distributions.

---

### Main Design Choices
* **LVM (Logical Volume Manager):** Partitioning was structured using LVM to allow flexible volume management and partition isolation (`/`, `/swap`, `/home`, `/srv`, `/var`, and `/var/log`). Isolating `/var/log` prevents log-flooding attacks from crashing the core system.
* **Security & Password Policy:** Enforced using `libpam-pwquality` to guarantee minimum character lengths, complexity (uppercase, lowercase, numbers), restriction of consecutive repeating characters, and exclusion of the username.
* **User Management:** Strict user/group hierarchies. Every user must belong to specific groups (e.g., `sudo`, `user42`), and sudo actions are logged and restricted.
* **Services Installed:** OpenSSH server configured securely on port `4242` (disallowing root login via SSH), UFW firewall blocking all unauthorized incoming traffic, AppArmor for mandatory access control, and a web server with WordPress (bonus implementation).

---

## 2. Comparative Technical Analysis

### Debian vs. Rocky Linux
| Feature | Debian | Rocky Linux |
| :--- | :--- | :--- |
| **Parent/Base** | Independent (Community-driven) | Downstream build of RHEL (Red Hat Enterprise Linux) |
| **Package Manager** | APT (`.deb` packages) | DNF / RPM (`.rpm` packages) |
| **Release Cycle** | Stable release every ~2 years | Aligned with RHEL enterprise releases |
| **Use Case** | Versatile general-purpose & community servers | Enterprise-grade server environments |

---

### AppArmor vs. SELinux
| Feature | AppArmor | SELinux |
| :--- | :--- | :--- |
| **Mechanism** | Path-based access control profiles | Label-based Mandatory Access Control (MAC) |
| **Complexity** | Easier to configure, read, and manage | Steeper learning curve, complex context labeling |
| **Default OS** | Debian, Ubuntu, openSUSE | RHEL, Rocky Linux, CentOS, Fedora |

---

### UFW vs. firewalld
| Feature | UFW (Uncomplicated Firewall) | firewalld |
| :--- | :--- | :--- |
| **Interface** | Front-end wrapper for `iptables` / `nftables` | Dynamic management tool with zones (`iptables` / `nftables`) |
| **Simplicity** | Designed to be user-friendly and straightforward | More advanced, zone-based routing architecture |
| **Default OS** | Debian, Ubuntu | RHEL, Rocky Linux, Fedora |

---

### VirtualBox vs. UTM
| Feature | VirtualBox | UTM |
| :--- | :--- | :--- |
| **Architecture** | Type-2 Hypervisor (x86_64 virtualization) | Built on QEMU (supports emulation & virtualization across architectures) |
| **Platform Compatibility** | Windows, macOS, Linux | Tailored primarily for macOS / Apple Silicon (ARM64) |
| **Ecosystem** | Mature industry standard with robust snapshot/NAT options | Modern frontend designed for macOS hardware capabilities |

---

## 3. Instructions

### Running the Virtual Machine
1. Open **VirtualBox** on your host machine.
2. Select your Born2beRoot virtual machine and click **Start**.
3. Log in using your user credentials at the console prompt.

---

### SSH Connection
To connect securely from your host terminal to the virtual machine via port `4242`, use the following command:
```bash
ssh username@127.0.0.1 -p 4242
