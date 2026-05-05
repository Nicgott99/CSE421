# Lab 4: Network Administration - DHCP and Dynamic Routing

## Lab Overview
Lab 4 covers practical implementation of DHCP (Dynamic Host Configuration Protocol) and dynamic routing protocols in enterprise networks. This comprehensive lab includes five practical tasks focusing on network scalability, automation, and dynamic route discovery.

## Lab Learning Objectives
By completing this lab, students will be able to:
- Configure DHCP servers and relay agents
- Implement centralized IP address management
- Deploy dynamic routing protocols in multi-router environments
- Enable automatic route discovery and selection
- Verify network functionality and troubleshoot connectivity issues

## Lab Tasks Overview

### Task 1: DHCP Configuration Using Cisco IOS
**Duration**: 2-3 hours
**Difficulty**: Intermediate
**Technologies**: Cisco IOS, DHCP, Router Configuration

**Key Concepts**:
- Router-based DHCP server configuration
- DHCP pool creation and management
- IP address exclusion
- Default gateway and DNS configuration
- DHCP helper addresses

**Outcomes**:
- Two DHCP pools (R1-LAN, R3-LAN) serving 192.168.10.0/24 and 192.168.30.0/24
- Automatic IP allocation to client devices
- Cross-subnet DHCP delivery via relay agents

[View Task 1 Details](./DHCP_Task1/Documentation/README.md)

---

### Task 2: DHCP Configuration Using Dedicated Server
**Duration**: 1.5-2 hours
**Difficulty**: Intermediate
**Technologies**: DHCP Server Appliance, Network Relay Agents

**Key Concepts**:
- Dedicated DHCP server implementation
- DHCP relay agents on routers
- Centralized IP pool management
- IP helper addresses configuration

**Outcomes**:
- Single point of DHCP management at 192.168.60.253
- Scalable architecture for enterprise networks
- Reduced router resource consumption
- Centralized lease policy enforcement

[View Task 2 Details](./DHCP_Task2/Documentation/README.md)

---

### Task 3: RIPv2 Dynamic Routing Protocol
**Duration**: 2.5-3 hours
**Difficulty**: Intermediate-Advanced
**Technologies**: RIPv2, Dynamic Routing, Multi-router Networks

**Key Concepts**:
- RIPv2 protocol configuration
- Network advertisement
- Automatic route discovery
- Passive interface configuration
- Default route propagation

**Outcomes**:
- Three routers (R1, R2, R3) running RIPv2
- Automatic route learning and convergence
- Multi-hop path selection
- Redundant connectivity

[View Task 3 Details](./Routing3/Documentation/README.md)

---

### Task 4: Static Routing - IPv4 Static and Default Routes
**Status**: Scheduled for next submission
- Configuring static routes
- Floating static routes
- Route prioritization
- Backup route configuration

---

### Task 5: Static Routing - Floating Static Routes
**Status**: Scheduled for next submission
- Advanced static routing scenarios
- Route preference and cost calculation
- Failover mechanisms

## Skills Demonstrated

| Skill | Tasks |
|-------|-------|
| **DHCP Configuration** | Task 1, Task 2 |
| **Cisco IOS Commands** | All Tasks |
| **Router Configuration** | All Tasks |
| **Network Design** | All Tasks |
| **IP Addressing** | All Tasks |
| **Protocol Understanding** | Task 1-3 |
| **Network Verification** | All Tasks |
| **Troubleshooting** | All Tasks |

## Equipment Used

- **Packet Tracer**: Version 8.x
- **Simulated Devices**:
  - Cisco Routers (1841, 2911)
  - PCs and End Devices
  - Switches
  - DHCP Server Appliance
- **Network Protocols**:
  - DHCP (UDP Port 67/68)
  - RIP (UDP Port 520)
  - IPv4

## File Structure

```
Lab4/
├── DHCP_Task1/
│   ├── Configuration_Files/
│   │   └── R2_DHCP_Config.txt
│   ├── Documentation/
│   │   └── README.md
│   └── 8.1.3.3_Packet_Tracer_-_Configuring_DHCPv4_Using_Cisco_IOS.pka
├── DHCP_Task2/
│   ├── Configuration_Files/
│   │   └── DHCP_Server_Config.txt
│   ├── Documentation/
│   │   └── README.md
│   └── 8.1.3.3_Packet_Tracer_-_Configuring_DHCPv4_Using_DHCP_Server.pka
├── Routing3/
│   ├── Configuration_Files/
│   │   └── RIPv2_Config.txt
│   ├── Documentation/
│   │   └── README.md
│   └── 7.3.1.8_Packet_Tracer_-_Configuring_RIPv2.pka
├── StaticRouting_Task1/ [TBD]
├── StaticRouting_Task2/ [TBD]
└── README.md
```

## How to Use These Resources

### For Learning
1. Read the task documentation in order (Task 1 → Task 3)
2. Review configuration files to understand CLI commands
3. Study the network topology and addressing scheme
4. Open Packet Tracer files for hands-on practice

### For Reference
- Use configuration files as command reference
- Consult documentation for protocol concepts
- Review verification commands for troubleshooting

### For Assessment
- Complete each task following the documentation
- Verify your configuration matches the provided commands
- Test connectivity using provided ping commands
- Document your results

## Key Technologies

### DHCP (Dynamic Host Configuration Protocol)
- Automates IP address assignment
- Reduces manual configuration errors
- Supports multiple subnets via relay agents
- Enables centralized network management

### RIPv2 (Routing Information Protocol v2)
- Simple distance-vector routing protocol
- Automatic route discovery
- VLSM support (unlike RIPv1)
- Suitable for medium-sized networks

### Cisco IOS
- Industry-standard routing operating system
- Command-line interface (CLI)
- Comprehensive routing and switching capabilities

## Learning Path Recommendation

**Week 1-2: DHCP Tasks**
- Understand DHCP client-server model
- Compare router-based vs. server-based approaches
- Practice configuration and verification

**Week 3: Routing Tasks**
- Learn dynamic routing principles
- Master RIPv2 configuration
- Explore route selection mechanisms

**Week 4: Advanced Tasks**
- Static routing strategies
- Route prioritization
- Failover mechanisms

## Assessment Criteria

Students are evaluated on:
- ✅ Correct configuration implementation
- ✅ Understanding of protocol operations
- ✅ Network verification and troubleshooting
- ✅ Documentation and explanation quality
- ✅ Professional presentation

## Resources Required

- **Software**: Cisco Packet Tracer (free download)
- **Time**: 10-15 hours total
- **Prerequisites**: Basic networking knowledge, OSI model understanding
- **Network Knowledge**: IP addressing, subnetting, routing basics

## Common Issues and Solutions

### DHCP Not Assigning Addresses
- Verify DHCP pool is created
- Check excluded addresses
- Confirm DHCP helper addresses on relay agents
- Verify client DHCP request transmission

### Routes Not Learning
- Verify RIP is enabled (`show ip protocols`)
- Check network statements match interface IPs
- Confirm passive interfaces on LANs
- Review debug output (`debug ip rip`)

### Connectivity Issues
- Ping between routers
- Verify interface IP assignments
- Check for duplicate network statements
- Review routing table (`show ip route`)

## Course Information

**Course**: CSE421 - Networking
**Institution**: BRAC University
**Semester**: Spring 2026
**Lab Coordinators**: MSMA, SRJ
**Theory Instructor**: AKTD

---

**Lab Completed By**:
- **Name**: MD HASIB ULLAH KHAN ALVIE
- **Student ID**: 22101371
- **Email**: hasibullah.khan.alvie@g.bracu.ac.bd
- **Completion Date**: May 2026

**Total Effort**: 9 Individual Contributions (DHCP Task 1, DHCP Task 2, Routing Task 3)

---

For questions or clarifications, refer to individual task documentation files or contact your lab coordinator.
