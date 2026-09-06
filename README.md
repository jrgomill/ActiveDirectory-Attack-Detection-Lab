# Active Directory Attack Simulation & Detection Lab

## Overview

This lab builds a small Active Directory environment, simulates common attacks
(password spraying, RDP brute-force, event log clearing, suspicious PowerShell),
and documents how to detect them using Windows Event Logs (and optionally a SIEM
such as Wazuh).

The goal is to demonstrate practical skills in:
- Active Directory engineering
- Attack simulation
- Detection engineering
- Log analysis and documentation

## Lab Architecture

- **Domain Controller**
  - Windows Server 2022
  - Roles: AD DS, DNS
- **Workstation**
  - Windows 10/11, domain-joined
- **Attacker VM (optional)**
  - Kali Linux or any Linux distro with Python

See `setup/vm-layout.md` for IP addressing and network layout.

## Attacks Implemented

- Password spraying against domain accounts
- RDP brute-force attempts
- Event log clearing (Security log)
- Suspicious PowerShell usage (encoded commands)

Each attack has:
- A script in `attacks/`
- A detection write-up in `detections/`
- Example screenshots in `screenshots/`

## How to Use This Repo

1. Build the lab following `setup/setup-guide.md`.
2. Run the attack scripts from the attacker VM or workstation.
3. Collect and analyze logs on the Domain Controller.
4. Use the detection guides in `detections/` to understand which Event IDs
   indicate malicious activity.

This project is intended for educational and defensive purposes only. Do not
run these techniques against systems you do not own or administer.
