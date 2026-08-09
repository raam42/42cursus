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
Es un software que simula un sistema de computación y puede ejecutar programas como si fuese una computadora real. Permite crear múltiples entornos simulados o recursos dedicados desde un solo sistema de hardware físico.

### 2. Why did you choose Debian?
Esto es algo personal para cada uno, mi opinión: El propio subject explica que es más sencillo hacerlo en Debian y si buscas documentación/tutoriales hay muchos y todos se han hecho en Debian.

### 3. Core Differences: Debian vs. Rocky Linux
| Aspect | Debian | Rocky Linux |
| :--- | :--- | :--- |
| **Base** | Independiente | RHEL |
| **Package Manager** | APT (`.deb`) | DNF (`.rpm`) |
| **Stability** | Flexible | Muy estable (empresas) |
| **Lifecycle / Support** | 3-5 años | 10 años |
| **Typical Use** | General | Servidores empresariales |

> **Resumen:** Debian es más versátil y comunitario. Rocky es una opción robusta y empresarial con soporte a largo plazo.

### 4. What is the purpose of Virtual Machines?
Su objetivo es el de proporcionar un entorno de ejecución independiente de la plataforma de hardware y del sistema operativo, que oculte los detalles de la plataforma subyacente y permita que un programa se ejecute siempre de la misma forma sobre cualquier plataforma.

### 5. Differences between `apt` and `aptitude`
Aptitude es una versión mejorada de apt. APT es un administrador de paquetes de nivel inferior y aptitude es un administrador de paquetes de alto nivel. Otra gran diferencia es la funcionalidad que ofrecen ambas herramientas. Aptitude ofrece una mejor funcionalidad en comparación con apt-get. Ambos son capaces de proporcionar los medios necesarios para realizar la gestión de paquetes. Sin embargo, si se busca un enfoque con más características, debería ser, Aptitude.

### 6. What is AppArmor?
Es un módulo de seguridad del kernel Linux que permite al administrador del sistema restringir las capacidades de un programa.

### 7. What is LVM?
Es un gestor de volúmenes lógicos. Proporciona un método para asignar espacio en dispositivos de almacenamiento masivo, que es más flexible que los esquemas de particionado convencionales para almacenar volúmenes.
