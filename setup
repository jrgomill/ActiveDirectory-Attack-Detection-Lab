# Active Directory Lab Setup Guide

## 1. Virtual Machines

- **DC01 (Domain Controller)**
  - OS: Windows Server 2022
  - CPU: 2 vCPU
  - RAM: 4–8 GB
  - Disk: 60 GB
- **WS01 (Workstation)**
  - OS: Windows 10/11
  - CPU: 2 vCPU
  - RAM: 4 GB
  - Disk: 40 GB
- **ATTACKER (optional)**
  - OS: Kali Linux / Ubuntu
  - CPU: 2 vCPU
  - RAM: 2–4 GB

All VMs on the same internal network (e.g., `10.0.0.0/24`).

## 2. Domain Controller Configuration

1. Install **Active Directory Domain Services** and **DNS**.
2. Promote the server to a domain controller:
   - Domain name: `lab.local`
3. Create test users:
   - `alice`, `bob`, `charlie`
   - Weak passwords for testing (e.g., `Password1!`).

## 3. Workstation Configuration

1. Join `WS01` to `lab.local`.
2. Log in as domain users to generate baseline activity.
3. Enable Remote Desktop on `WS01` for RDP brute-force testing.

## 4. Logging Configuration

On **DC01**:

- Enable **Advanced Audit Policy**:
  - Account Logon
  - Logon/Logoff
  - Account Management
  - Object Access
- Ensure Security log size is increased (e.g., 512 MB).
- Optionally enable PowerShell logging:
  - Module logging
  - Script block logging

See `detections/` for specific Event IDs used in this lab.

