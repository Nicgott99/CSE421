# DHCP Task 1: Configuring DHCPv4 Using Cisco IOS

## Overview
This task involves configuring DHCP (Dynamic Host Configuration Protocol) v4 on a Cisco router to dynamically assign IP addresses to connected clients.

## Objectives
- Configure DHCP pools on Router R2
- Set up DHCP helper addresses on R1 and R3
- Exclude specific IP addresses from DHCP allocation
- Verify DHCP functionality through client connectivity

## Network Topology
- **Router R2**: DHCP Server
- **Router R1**: DHCP Relay Agent for R1-LAN (192.168.10.0/24)
- **Router R3**: DHCP Relay Agent for R3-LAN (192.168.30.0/24)
- **DNS Server**: 192.168.20.254

## Configuration Details

### DHCP Pools Configuration
Two DHCP pools were configured:
1. **R1-LAN Pool**: 192.168.10.0/24
   - Gateway: 192.168.10.1
   - DNS: 192.168.20.254

2. **R3-LAN Pool**: 192.168.30.0/24
   - Gateway: 192.168.30.1
   - DNS: 192.168.20.254

### Excluded Addresses
- **R1-LAN**: 192.168.10.1 - 192.168.10.10 (reserved for network equipment)

### DHCP Helper Addresses
- **R1**: ip helper-address 10.1.1.2
- **R3**: ip helper-address 10.2.2.2

## Verification Commands
```
show ip dhcp binding      - View active DHCP leases
show ip dhcp pool         - Display DHCP pool statistics
ping <IP>               - Test connectivity
```

## Learning Outcomes
- Understanding DHCP server configuration
- Implementing DHCP relay agents
- Network address allocation and reservation
- Client-server communication over multiple subnets

---
**Completed By**: MD HASIB ULLAH KHAN ALVIE
**Student ID**: 22101371
**Course**: CSE421
**Lab Faculty**: MSMA, SRJ
