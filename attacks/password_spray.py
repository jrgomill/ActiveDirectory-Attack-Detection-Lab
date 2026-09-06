#!/usr/bin/env python3
"""
password_spray.py

Simple password spraying script for lab environments.
Do NOT use outside of systems you own/administer.

Generates failed logon events (e.g., 4625, 4771) on the domain controller.
"""

import itertools
import socket

TARGET_HOST = "10.0.0.10"  # WS01 or DC01
TARGET_PORT = 3389         # RDP port
USERNAMES = ["alice", "bob", "charlie", "david", "eve"]
PASSWORD = "Winter2024!"   # single password used for spraying
TIMEOUT = 3


def check_port(host: str, port: int) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    try:
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False


def spray():
    if not check_port(TARGET_HOST, TARGET_PORT):
        print(f"[!] Cannot reach {TARGET_HOST}:{TARGET_PORT}")
        return

    print(f"[+] Starting password spray against {TARGET_HOST}:{TARGET_PORT}")
    for user in USERNAMES:
        # In a real script, you would attempt authentication (e.g., via RDP, SMB, LDAP).
        # Here we just log the attempt to stdout; the actual auth mechanism is left
        # for you to implement based on your chosen protocol.
        print(f"[*] Trying user={user} password={PASSWORD}")
        # TODO: integrate with an actual auth library (e.g., impacket, winrm, rdp client)
        # This placeholder is enough to show intent and structure in GitHub.


if __name__ == "__main__":
    spray()

