# clear_event_logs.ps1
# Clears the Security event log to generate Event ID 1102.

Write-Host "[*] Clearing Security event log..."
wevtutil cl Security
Write-Host "[+] Security event log cleared. Check DC01 for Event ID 1102."

