# Router Configuration Details

## Configuration Overview

This document provides a detailed breakdown of the router configurations implemented in this assignment.

## Router 1 (R1) Configuration

### Device Identification
```
hostname R1
```
Sets the device name to "R1" for easy identification in the network.

### System Security

#### Enable Secret Password
```
enable secret class
```
- Provides password-protected access to privileged EXEC mode
- Uses MD5 encryption
- Password: "class"

#### Console Access Security
```
line console 0
password cisco
login
```
- Restricts console port access
- Requires password authentication
- Password: "cisco"

#### VTY (Virtual Terminal) Access Security
```
line vty 0 4
password cisco
login
```
- Restricts Telnet access (lines 0-4 allow 5 simultaneous connections)
- Requires password authentication
- Password: "cisco"

#### Save Configuration
```
copy running-config startup-config
```
- Persists configuration to NVRAM
- Ensures configuration survives router reboot

### Interface Configuration

#### FastEthernet Interface (LAN)
```
interface FastEthernet0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
```
- Primary LAN interface
- Network: 192.168.1.0/24
- Connects to local network devices
- Gateway IP for the subnet

#### Serial Interface (WAN)
```
interface Serial0/0/0
ip address 192.168.2.1 255.255.255.0
clock rate 64000
no shutdown
```
- WAN connection to Router 2
- Network: 192.168.2.0/24
- Clock rate 64,000 bps (DCE providing clock signal)
- Point-to-point link

---

## Router 2 (R2) Configuration

### Device Identification
```
hostname R2
```
Sets the device name to "R2".

### System Security

Security configuration is identical to Router 1:
- Enable Secret: "class"
- Console Password: "cisco"
- VTY Password: "cisco"

### Interface Configuration

#### Serial Interface (WAN)
```
interface Serial0/0/0
ip address 192.168.2.2 255.255.255.0
no shutdown
```
- WAN connection to Router 1
- Network: 192.168.2.0/24
- DTE interface (no clock rate required)
- Receives clock signal from R1

#### FastEthernet Interface (LAN)
```
interface FastEthernet0/0
ip address 192.168.3.1 255.255.255.0
no shutdown
```
- Primary LAN interface
- Network: 192.168.3.0/24
- Gateway IP for the subnet

---

## Network Connectivity Summary

| Device | Interface | IP Address | Subnet Mask | Purpose |
|--------|-----------|-----------|-------------|---------|
| R1 | F0/0 | 192.168.1.1 | 255.255.255.0 | LAN Gateway |
| R1 | S0/0/0 | 192.168.2.1 | 255.255.255.0 | WAN (DCE) |
| R2 | S0/0/0 | 192.168.2.2 | 255.255.255.0 | WAN (DTE) |
| R2 | F0/0 | 192.168.3.1 | 255.255.255.0 | LAN Gateway |

---

## Security Implementation Summary

| Security Element | Configuration | Password |
|------------------|---------------|----------|
| Privileged Access | Enable Secret | class |
| Console Access | Password Protected | cisco |
| Remote Access (Telnet) | Password Protected | cisco |
| Configuration Backup | Running → Startup | - |

---

## Additional Notes

- **No Domain Lookup**: Disabled with `no ip domain-lookup` to prevent router from attempting to resolve mistyped commands as IP addresses
- **Clock Rate**: Set on R1 serial interface (DCE) to synchronize with R2 (DTE)
- **Auto-shutdown Prevention**: `no shut` command ensures interfaces are active upon configuration
- **Configuration Persistence**: Running configuration is saved to startup configuration to survive router resets

---

**Created**: May 2026
**Lab Faculty**: MSMA and SRJ
**Course**: CSE421 - Networking Protocols and Interconnection
