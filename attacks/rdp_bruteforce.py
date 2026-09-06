#!/usr/bin/env python3
"""
rdp_bruteforce.py

Brute-force style RDP username/password attempts for lab use.
Intended to generate multiple 4625 failed logon events.
"""

USERNAMES = ["alice", "bob"]
PASSWORDS = ["Password1!", "Password2!", "Password3!"]

def brute_force():
    for user in USERNAMES:
        for pwd in PASSWORDS:
            print(f"[*] Attempting RDP login user={user} password={pwd}")
            # TODO: integrate with an RDP client library or external tool.
            # This script is primarily for documentation and structure.

if __name__ == "__main__":
    brute_force()

