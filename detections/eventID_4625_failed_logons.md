# Event ID 4625 – Failed Logon Attempts

## Description

Event ID 4625 is generated when a logon attempt fails. In this lab, we use
password spraying and RDP brute-force scripts to generate multiple 4625 events.

## Where to Look

- **Host:** Domain Controller (DC01)
- **Log:** Security
- **Event ID:** 4625

## Fields of Interest

- `Account Name`
- `Logon Type`
- `Failure Information` (Status, Sub Status)
- `Source Network Address`

## Detection Idea

- Threshold-based rule:
  - More than N failed logons from the same IP in M minutes.
- Spray pattern:
  - Same password, multiple usernames from one source.

## Example Use Case

Run `attacks/password_spray.py` and then open Event Viewer on DC01:

- Filter Security log for Event ID 4625.
- Observe multiple failed logons with different `Account Name` values and the
  same `Source Network Address`.

