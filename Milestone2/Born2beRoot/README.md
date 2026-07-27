*This project has been created as part of the 42 curriculum by rodrigoa.*

## Project Description
Born2beRoot is a project designed to introduce us to system administration by creating our first strict and secure server using Debian. The primary goal is to build a virtualized infrastructure from scratch that complies with rigorous security policies regarding passwords, firewalls, user management, SSH access control, and automated system monitoring.

---

## Operating System Choice: Debian vs. Rocky Linux

For this project, I chose **Debian**. 

* **Debian**: 
  * *Advantages*: It is an extremely stable, lightweight system ideal for headless servers, with a massive community and extensive documentation. It uses the `apt`/`aptitude` package manager and the AppArmor security framework.
  * *Disadvantages*: Software packages can be more conservative and older compared to bleeding-edge distributions, prioritizing stability over the latest features.
* **Rocky Linux**: 
  * *Advantages*: It is a direct downstream successor of CentOS, heavily oriented toward enterprise environments and Red Hat Enterprise Linux (RHEL). It uses `DNF` and the Mandatory Access Control system `SELinux`.
  * *Disadvantages*: For a user starting out in Unix system administration, the syntax and policy management with SELinux have a considerably steeper learning curve.

---

## Main Design Choices

* **Partitioning (LVM)**: Logical Volume Manager (LVM) with encryption was used to divide the disk into logical partitions (`/`, `/boot`, `/home`, `/var`, `/srv`, `/tmp`), ensuring flexibility in space management and security against physical unauthorized access.
* **Security Policies**: 
  * Strict password complexity rules were implemented using `libpam-pwquality` (minimum length, prohibition of sequences or the username).
  * Password aging was configured via `/etc/login.defs` (30-day expiration, 7-day warning).
* **User Administration**: Specific groups like `sudo` and `user42` were created to restrict administrative privileges, forcing regular users to operate via audited commands.
* **Network Services**: Remote access was restricted using exclusively the custom port `4242` for SSH, completely blocking direct root login, and an active firewall was implemented using `UFW`.

---

## Technology Comparisons

### Debian vs. Rocky Linux
* **Debian** prioritizes absolute stability based on free software, managing packages via `apt`/`aptitude` and AppArmor. **Rocky Linux** focuses on the Red Hat-compatible enterprise ecosystem, using RPM packages (`DNF`) and SELinux security.

### AppArmor vs. SELinux
* **AppArmor** uses file path-based profiles to restrict program capabilities, making it more intuitive and easier to debug. **SELinux** (Security-Enhanced Linux) uses Mandatory Access Control security labels assigned to every process and file, offering superior security granularity but with noticeably higher configuration complexity.

### UFW vs. firewalld
* **UFW (Uncomplicated Firewall)** is a simplified frontend for `iptables`/`nftables` designed to be intuitive and easy to configure via simple rule commands. **firewalld** uses network zones and allows dynamic rule management without interrupting active connections, making it more common in Red Hat-oriented corporate environments.

### VirtualBox vs. UTM
* **VirtualBox** is a classic, cross-platform Type-2 hypervisor (Windows, Linux, macOS) widely compatible for traditional x86_64 virtualization. **UTM** is a virtualization solution based on QEMU optimized natively for macOS systems (Apple Silicon and Intel), ideal for leveraging hardware acceleration on Mac machines.