# Event ID 4104 – PowerShell Script Block Logging

## Description

Event ID **4104** is generated when PowerShell executes a script block and
PowerShell Script Block Logging is enabled. This event provides visibility into
PowerShell commands — including encoded, obfuscated, or malicious scripts.

In this lab, the `suspicious_powershell.ps1` script triggers Event ID 4104 using
an encoded command to simulate attacker behavior.

---

## Where to Look

- **Host:** Domain Controller (DC01) or Workstation (WS01)
- **Log:** Microsoft-Windows-PowerShell/Operational
- **Event ID:** 4104  
- **Source:** PowerShell

---

## Why This Matters

PowerShell is a common attacker tool for:

- Reconnaissance  
- Credential harvesting  
- Lateral movement  
- Payload execution  
- Defense evasion  

Encoded commands (`-EncodedCommand`) are frequently used to hide malicious
behavior.

Event ID 4104 provides defenders with visibility into these actions.

---

## Fields of Interest

- `ScriptBlockText` – the actual PowerShell code executed  
- `UserId` – user running the command  
- `ProcessId` – PID of the PowerShell process  
- `CommandLine` – includes `-EncodedCommand` if used  
- `TimeCreated` – timestamp of execution  

---

## Detection Ideas

### **1. Encoded Command Detection**
Alert when:
- `CommandLine` contains `EncodedCommand`
- `ScriptBlockText` contains suspicious patterns

### **2. Parent-Child Process Analysis**
Combine with Sysmon Event ID 1:
- PowerShell spawning `cmd.exe`
- PowerShell spawning `rundll32.exe`
- PowerShell spawning `wscript.exe`

### **3. MITRE ATT&CK Mapping**
- **T1059.001 – PowerShell**

---

## Example Use Case

Run:


