# LAB REPORT: BASIC ROUTER CONFIGURATION

## Assignment Information

| Field | Value |
|-------|-------|
| **Course** | CSE421: Networking Protocols and Interconnection |
| **Assignment** | Lab 1 - Basic Router Configuration |
| **Student Name** | MD HASIB ULLAH KHAN ALVIE |
| **Student ID** | 22101371 |
| **Semester** | Spring 2026 |
| **Lab Faculty** | MSMA and SRJ |
| **Submission Date** | May 2026 |
| **University** | BRAC University |

---

## Executive Summary

This lab assignment focused on the fundamental configuration of Cisco routers using Cisco Packet Tracer. The objective was to configure two routers with basic security settings, interface configurations, and network connectivity. The assignment reinforced understanding of:

- Cisco Internetwork Operating System (IOS) command structure
- Router configuration modes and command hierarchy
- Network security implementation on routers
- IP addressing and interface configuration
- Router-to-router connectivity via serial interfaces

**Status**: ✅ **COMPLETED SUCCESSFULLY**

---

## Objectives

### Primary Objectives
1. Configure basic router settings (hostname, system clock, banners)
2. Implement authentication and security protocols
3. Configure network interfaces (LAN and WAN)
4. Establish inter-router connectivity
5. Verify and save router configurations

### Learning Outcomes
Upon completion, students should understand:
- The different operational modes in Cisco IOS
- Password protection mechanisms (Enable Secret, Console, VTY)
- Interface configuration and IP addressing
- The role of serial interfaces in WAN connectivity
- Clock rate configuration in DCE/DTE environments

---

## Network Topology

```
┌─────────────────────────────────────────────────────┐
│                  Network Topology                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│    Router 1 (R1)              Router 2 (R2)        │
│    ──────────────              ──────────────       │
│                                                     │
│   S0/0/0 ────────────────────── S0/0/0             │
│   (DCE)      192.168.2.0/24      (DTE)             │
│   .1              Backbone            .2            │
│    │                                    │            │
│    │ F0/0                          F0/0 │            │
│    │ (LAN)                         (LAN) │            │
│ 192.168.1.0/24                  192.168.3.0/24    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Connectivity Matrix

| Device | Interface | IP Address | Subnet Mask | Type | Role |
|--------|-----------|-----------|-------------|------|------|
| R1 | F0/0 | 192.168.1.1 | 255.255.255.0 | LAN | Gateway |
| R1 | S0/0/0 | 192.168.2.1 | 255.255.255.0 | WAN | DCE (Master) |
| R2 | S0/0/0 | 192.168.2.2 | 255.255.255.0 | WAN | DTE (Slave) |
| R2 | F0/0 | 192.168.3.1 | 255.255.255.0 | LAN | Gateway |

---

## Configuration Implementation

### Router 1 (R1) Configuration Steps

#### Step 1: Access Privileged Mode
```
Router>enable
Router#
```

#### Step 2: Enter Global Configuration Mode
```
Router#configure terminal
Router(config)#
```

#### Step 3: Set Device Name
```
Router(config)#hostname R1
R1(config)#
```
**Purpose**: Identifies the device in the network for easier management and identification.

#### Step 4: Disable DNS Lookups
```
R1(config)#no ip domain-lookup
```
**Purpose**: Prevents router from attempting to resolve mistyped commands as IP addresses, improving response time.

#### Step 5: Set Enable Secret Password
```
R1(config)#enable secret class
```
**Purpose**: Encrypts password used to enter privileged EXEC mode. Uses MD5 encryption.
**Password**: class

#### Step 6: Configure Banner
```
R1(config)#banner motd & Welcome to Router 1 &
```
**Purpose**: Displays a message of the day when users connect to the router.

#### Step 7: Configure Console Line Security
```
R1(config)#line console 0
R1(config-line)#password cisco
R1(config-line)#login
R1(config-line)#exit
```
**Purpose**: Requires password authentication for direct console access.
**Password**: cisco

#### Step 8: Configure VTY (Telnet) Security
```
R1(config)#line vty 0 4
R1(config-line)#password cisco
R1(config-line)#login
R1(config-line)#exit
```
**Purpose**: Requires password authentication for remote Telnet access (lines 0-4 allow 5 simultaneous connections).
**Password**: cisco

#### Step 9: Configure FastEthernet Interface (LAN)
```
R1(config)#interface FastEthernet0/0
R1(config-if)#ip address 192.168.1.1 255.255.255.0
R1(config-if)#no shutdown
R1(config-if)#exit
```
**Purpose**: Configures the LAN interface with IP address and activates the port.

#### Step 10: Configure Serial Interface (WAN)
```
R1(config)#interface Serial0/0/0
R1(config-if)#ip address 192.168.2.1 255.255.255.0
R1(config-if)#clock rate 64000
R1(config-if)#no shutdown
R1(config-if)#exit
```
**Purpose**: Configures the WAN interface. Since R1 is the DCE, it provides the clock signal (64 kbps).

#### Step 11: Save Configuration
```
R1(config)#end
R1#copy running-config startup-config
```
**Purpose**: Saves the running configuration to NVRAM, ensuring it persists after router reboot.

---

### Router 2 (R2) Configuration Steps

Router 2 configuration is similar to Router 1, with the following differences:

**Key Differences:**
1. Hostname: R2
2. FastEthernet IP: 192.168.3.1 (instead of 192.168.1.1)
3. Serial Interface: DTE (no clock rate required; receives clock from R1)
4. All security passwords remain the same

**Full Configuration:**
```
Router#configure terminal
Router(config)#hostname R2
R2(config)#no ip domain-lookup
R2(config)#enable secret class
R2(config)#banner motd & Welcome to Router 2 &
R2(config)#line console 0
R2(config-line)#password cisco
R2(config-line)#login
R2(config-line)#exit
R2(config)#line vty 0 4
R2(config-line)#password cisco
R2(config-line)#login
R2(config-line)#exit
R2(config)#interface Serial0/0/0
R2(config-if)#ip address 192.168.2.2 255.255.255.0
R2(config-if)#no shutdown
R2(config-if)#exit
R2(config)#interface FastEthernet0/0
R2(config-if)#ip address 192.168.3.1 255.255.255.0
R2(config-if)#no shutdown
R2(config-if)#end
R2#copy running-config startup-config
```

---

## Verification and Testing

### Verification Commands Used

1. **Display Running Configuration**
   ```
   Router#show running-config
   ```
   Verifies all configurations are correctly applied.

2. **Display Interface Information**
   ```
   Router#show interfaces
   ```
   Shows detailed information about all interfaces.

3. **Display IP Interface Brief**
   ```
   Router#show ip interface brief
   ```
   Shows quick summary of interface status and IP addresses.

4. **Connectivity Testing**
   ```
   Router#ping 192.168.2.2
   ```
   Tests connectivity between routers via WAN connection.

### Test Results

| Test | Expected Result | Actual Result | Status |
|------|-----------------|---------------|--------|
| R1 Console Access | Requires password | Requires password | ✅ PASS |
| R1 Telnet Access | Requires password | Requires password | ✅ PASS |
| R1 Enable Mode | Requires secret | Requires secret | ✅ PASS |
| R2 Console Access | Requires password | Requires password | ✅ PASS |
| R2 Enable Mode | Requires secret | Requires secret | ✅ PASS |
| R1 F0/0 Active | Interface UP | Interface UP | ✅ PASS |
| R1 S0/0/0 Active | Interface UP | Interface UP | ✅ PASS |
| R2 S0/0/0 Active | Interface UP | Interface UP | ✅ PASS |
| R2 F0/0 Active | Interface UP | Interface UP | ✅ PASS |
| R1 → R2 Ping | Successful | Successful | ✅ PASS |
| R2 → R1 Ping | Successful | Successful | ✅ PASS |

---

## Key Concepts Demonstrated

### 1. Cisco IOS Command Structure
- User EXEC Mode (Router>)
- Privileged EXEC Mode (Router#)
- Global Configuration Mode (config)
- Interface-specific Configuration Mode (config-if)
- Line-specific Configuration Mode (config-line)

### 2. Security Implementation
- **Enable Secret**: Encrypts privileged access passwords
- **Console Password**: Secures local console access
- **VTY Password**: Secures remote Telnet access
- **Login Authentication**: Enforces credential checks

### 3. Interface Configuration
- **LAN Interfaces (FastEthernet)**: For local network connectivity
- **WAN Interfaces (Serial)**: For point-to-point remote connections
- **Interface Status**: Active/Inactive states managed by "shutdown/no shutdown"

### 4. Network Addressing
- **Subnetting**: Proper subnet mask application
- **IP Address Planning**: Non-overlapping network ranges
- **Gateway Configuration**: Each router serves as gateway for its LAN

### 5. Configuration Management
- **Running Configuration**: Active configuration in RAM
- **Startup Configuration**: Saved configuration in NVRAM
- **Configuration Persistence**: Ensures settings survive reboot

---

## Challenges Encountered

### Minor Challenges
1. **Clock Rate Configuration**: Initially questioned on DTE vs. DCE roles; clarified that only DCE (R1) requires clock rate.
2. **Password Security**: Understood difference between "enable secret" (encrypted) and "enable password" (plaintext).
3. **Interface Shutdown State**: Learned that new interfaces default to "shut" state and require "no shutdown."

### Solutions Applied
- Reviewed Cisco IOS command reference documentation
- Referred to course materials on DCE/DTE synchronization
- Tested in Packet Tracer before finalizing configuration

---

## Lessons Learned

1. **Command Sequence Matters**: Order of commands affects configuration validity
2. **Security Priority**: Multiple layers of password protection are essential in network infrastructure
3. **Interface Management**: Both physical activation (no shutdown) and logical configuration (IP address) are necessary
4. **Backup Configurations**: Always save running-config to startup-config for persistence
5. **Testing Before Deployment**: Verification commands validate configuration correctness

---

## Conclusion

This lab assignment successfully demonstrated the ability to configure Cisco routers with appropriate security settings, network interfaces, and inter-device connectivity. The assignment reinforced fundamental Cisco IOS command structure and best practices for network device configuration.

### Summary of Achievements
- ✅ Configured 2 routers with proper hostnames and system settings
- ✅ Implemented 3-layer password protection (Enable Secret, Console, VTY)
- ✅ Configured 4 network interfaces (2 LAN, 2 WAN)
- ✅ Established successful inter-router connectivity
- ✅ Documented all configurations and procedures
- ✅ Verified all functionality through testing

### Recommendations for Future Work
1. Explore Static Routing protocols for inter-network communication
2. Investigate Dynamic Routing Protocols (RIP, OSPF, EIGRP)
3. Implement Access Control Lists (ACLs) for enhanced security
4. Study VPN configuration for secure remote access
5. Practice disaster recovery and configuration backup procedures

---

## Appendices

### Appendix A: Complete Configuration Files
- **R1_Config.txt**: Contains full Router 1 configuration
- **R2_Config.txt**: Contains full Router 2 configuration
- **Commands_Original.txt**: Original assignment commands reference

### Appendix B: Files Included
- **Basic_Router_Config.pka**: Cisco Packet Tracer simulation file
- **Assignment_Specification.pdf**: Original assignment requirements
- **Documentation files**: Detailed configuration explanations

### Appendix C: Reference Materials
- Cisco IOS Command Reference Manual
- BRAC University CSE421 Course Materials
- RFC 791: Internet Protocol (IPv4)
- Cisco Official Training Videos

---

**Report Prepared By**: MD HASIB ULLAH KHAN ALVIE  
**Student ID**: 22101371  
**Date**: May 2026  
**Course**: CSE421 - Networking Protocols and Interconnection  
**University**: BRAC University  
**Lab Faculty**: MSMA and SRJ  

---

**Status**: ✅ ASSIGNMENT COMPLETE AND VERIFIED
