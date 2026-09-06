# suspicious_powershell.ps1
# Example of encoded PowerShell command to trigger Event ID 4104.

$command = 'Write-Host "This is a test of suspicious PowerShell activity"'
$bytes   = [System.Text.Encoding]::Unicode.GetBytes($command)
$encoded = [Convert]::ToBase64String($bytes)

Write-Host "[*] Running encoded PowerShell command..."
powershell.exe -EncodedCommand $encoded

