# Event ID 1102 – Security Event Log Cleared

## Description

Event ID **1102** is generated when the Windows Security event log is cleared.
This is a high‑severity defense evasion technique commonly used by attackers to
remove evidence of brute-force attempts, privilege escalation, or other malicious
activity.

In this lab, the `clear_event_logs.ps1` script intentionally triggers Event ID
1102 to demonstrate how defenders can detect log tampering.

---

## Where to Look

- **Host:** Domain Controller (DC01)
- **Log:** Security
- **Event ID:** 1102  
- **Source:** Microsoft-Windows-Eventlog

---

## Why This Matters

Clearing the Security log is extremely rare during normal operations.  
When it happens, it almost always indicates:

- An attacker attempting to cover their tracks  
- A compromised administrator account  
- Malicious PowerShell or command-line activity  

