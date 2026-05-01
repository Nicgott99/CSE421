# Assignment 1: Basic Router Configuration

## 📌 Overview

This assignment focuses on the fundamental configuration of Cisco routers. Students are required to configure multiple routers in a network topology, set up security parameters, and establish inter-router connectivity through serial interfaces.

## 🎯 Assignment Objectives

Upon completion of this assignment, students will be able to:

1. **Configure Router Basics**
   - Set router hostnames for device identification
   - Disable DNS lookups to improve command response time
   - Configure banner messages (Message of the Day)

2. **Implement Security Measures**
   - Set enable secret passwords with encryption
   - Configure console and VTY (virtual terminal) passwords
   - Implement login authentication on privileged and user modes

3. **Configure Network Interfaces**
   - Assign IP addresses to FastEthernet interfaces
   - Configure serial interfaces for WAN connectivity
   - Set appropriate clock rates on DCE devices
   - Enable interfaces using the "no shutdown" command

4. **Save and Verify Configuration**
   - Copy running configuration to startup configuration
   - Verify configuration persistence
   - Understand configuration backup and recovery

## 📋 Equipment and Resources

| Resource | Details |
|----------|---------|
| **Simulator** | Cisco Packet Tracer 8.x |
| **IOS Version** | Cisco IOS 15.x |
| **Devices** | 2 Cisco Routers |
| **Interfaces** | FastEthernet (LAN), Serial (WAN) |

## 🔧 Configuration Parameters

### Network Topology

```
Router 1 (R1)          Router 2 (R2)
────────────────────────────────
F0/0: 192.168.1.0/24   F0/0: 192.168.3.0/24
      │                      │
      └──────S0/0/0 ─────────S0/0/0
         192.168.2.0/24 backbone
```

### Common Configuration Settings

| Setting | Value |
|---------|-------|
| Enable Secret | class |
| Console Password | cisco |
| VTY Password | cisco |
| Hostname Prefix | R (e.g., R1, R2) |

## ⚙️ Key Concepts

### Configuration Modes

- **User EXEC Mode** (`Router>`) - Basic device monitoring
- **Privileged EXEC Mode** (`Router#`) - Configuration access
- **Global Configuration Mode** (`Router(config)#`) - Device-wide settings
- **Interface Configuration Mode** (`Router(config-if)#`) - Per-interface settings
- **Line Configuration Mode** (`Router(config-line)#`) - Access line settings

### Interface Types

- **FastEthernet (F0/0)** - LAN interface for local network connectivity
- **Serial (S0/0/0)** - WAN interface for point-to-point connections

## 📚 Related Concepts

- **Cisco IOS Command Line Interface (CLI)**
- **Router Boot Sequence**
- **Configuration Files (NVRAM, RAM, Flash)**
- **Router Memory Types**
- **Basic Cisco Command Syntax**

## ✅ Tasks Completed

- [x] Router 1 basic configuration
- [x] Router 2 basic configuration
- [x] Interface configuration for both routers
- [x] Security implementation (passwords and authentication)
- [x] Configuration backup (running → startup)
- [x] Network verification

## 📝 Assessment Criteria

| Criteria | Points |
|----------|--------|
| Router 1 Configuration | 25 |
| Router 2 Configuration | 25 |
| Security Implementation | 20 |
| Interface Configuration | 20 |
| Documentation | 10 |
| **Total** | **100** |

## 🔗 References and Resources

- Cisco IOS Command Reference
- Cisco Official Training Materials
- RFC 791 - Internet Protocol (IPv4)
- RFC 1195 - Use of OSI IS-IS for Routing in TCP/IP and Dual Environments

---

**Assignment Date**: Spring 2026
**Submission Status**: ✅ Completed
**Instructor**: MSMA and SRJ (Lab Faculty)
