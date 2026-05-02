# Assignment 2: Application Layer Protocols and Network Simulation

## 📌 Overview

This assignment focuses on understanding application layer protocols (HTTP and SMTP) and implementing network simulations using NS-3 (Network Simulator 3). Students gain practical experience with protocol analysis, packet inspection, and network performance measurement through simulation.

## 🎯 Assignment Objectives

Upon completion of this assignment, students will be able to:

1. **Understand Application Layer Protocols**
   - HTTP (HyperText Transfer Protocol) - Request/Response model
   - SMTP (Simple Mail Transfer Protocol) - Email transmission
   - Protocol headers, methods, and communication flow
   - Packet structure and field meanings

2. **Analyze Network Packets**
   - Capture and inspect HTTP packets
   - Identify protocol fields and parameters
   - Understand packet flow and communication sequences
   - Analyze packet headers and payloads

3. **Implement Network Simulations**
   - Configure NS-3 network topology
   - Create point-to-point links
   - Configure network devices and protocols
   - Implement application-layer services
   - Measure network performance metrics

4. **Measure Network Performance**
   - Calculate throughput
   - Measure packet loss
   - Calculate latency and delay
   - Analyze flow statistics
   - Generate performance reports

## 📋 Topics Covered

### 1. Application Layer Protocols
- **HTTP/1.1** Protocol fundamentals
- **SMTP** Protocol for email transmission
- Protocol methods and status codes
- Client-server model
- Request-response cycle

### 2. Network Protocol Analysis
- Packet structure analysis
- TCP/UDP segments
- Protocol headers and payloads
- Wireshark packet inspection
- Traffic analysis and interpretation

### 3. Network Simulation (NS-3)
- NS-3 architecture and components
- Node and device creation
- Network topology design
- Channel configuration
- Application layer modeling

### 4. Performance Metrics
- Throughput measurement
- Latency and delay calculation
- Packet loss analysis
- Flow monitoring
- Statistical analysis

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **NS-3** | Network simulation and modeling |
| **Python** | NS-3 scripting and simulation control |
| **UDP** | Transport protocol for echo service |
| **Flow Monitor** | Network performance measurement |
| **Wireshark** | Packet capture and analysis |

## 📚 Network Simulation Details

### Topology Used

```
Point-to-Point Network (10.1.1.0/24)
│
├─ Node 0 (UDP Echo Client)
│  └─ Interface: 10.1.1.1
│
└─ Node 1 (UDP Echo Server)
   └─ Interface: 10.1.1.2

Link Characteristics:
- Data Rate: 5 Mbps
- Delay: 2 ms
- MTU: Standard (1500 bytes)
```

### Simulation Parameters

| Parameter | Value |
|-----------|-------|
| Data Rate | 5 Mbps |
| Link Delay | 2 ms |
| Packet Size | 2048 bytes |
| Simulation Duration | 20 seconds |
| Server Start Time | 1.0 second |
| Client Start Time | 2.0 seconds |

### Application Configuration

- **Protocol**: UDP Echo
- **Server Port**: 9
- **Max Packets**: 1
- **Interval**: 1.0 second
- **Packet Size**: 2048 bytes

## 📊 Performance Metrics Measured

The simulation measures and reports:

1. **Throughput**
   - Transmitted bytes
   - Received bytes
   - Calculation: (RxBytes × 8) / Duration (in bits/second)

2. **Packet Statistics**
   - Transmitted packets
   - Received packets
   - Lost packets
   - Delivery ratio

3. **Delay Analysis**
   - Mean delay (milliseconds)
   - Delay sum calculation
   - Per-packet latency

4. **Flow Information**
   - Source and destination addresses
   - Source and destination ports
   - Protocol type (TCP/UDP)
   - Flow identification

## 🔧 Key Concepts

### HTTP Protocol
- Request methods: GET, POST, PUT, DELETE, etc.
- Status codes: 200 OK, 404 Not Found, 500 Server Error, etc.
- Headers: Content-Type, Content-Length, Authorization
- Message format: Request line, Headers, Body

### SMTP Protocol
- SMTP commands: MAIL, RCPT, DATA, QUIT
- Response codes: 250 OK, 550 User Unknown
- Connection establishment and closure
- Email message format

### NS-3 Components
- **NodeContainer**: Collection of nodes in simulation
- **NetDeviceContainer**: Collection of network interfaces
- **Ipv4InterfaceContainer**: IP address assignment
- **ApplicationContainer**: Application instances
- **FlowMonitor**: Performance measurement tool

### Network Performance
- **Throughput**: Data transferred per unit time (bits/second)
- **Latency**: Time for packet to travel from source to destination
- **Packet Loss**: Percentage of packets not received
- **Jitter**: Variation in packet arrival times

## ✅ Tasks Completed

- [x] HTTP/SMTP protocol analysis and documentation
- [x] Packet capture and inspection
- [x] NS-3 simulation environment setup
- [x] Network topology configuration (point-to-point)
- [x] UDP echo application implementation
- [x] Performance metrics measurement
- [x] Flow statistics collection and analysis
- [x] Performance report generation

## 📝 Assignment Deliverables

| Item | Description | Status |
|------|-------------|--------|
| HTTP/SMTP Analysis | Protocol documentation and examples | ✅ |
| Packet Analysis | Captured packet inspection and interpretation | ✅ |
| NS3 Simulation Code | Functional Python simulation script | ✅ |
| Performance Report | Measured metrics and analysis | ✅ |
| Documentation | Comprehensive assignment documentation | ✅ |

## 🔗 References and Resources

- RFC 2616: Hypertext Transfer Protocol (HTTP/1.1)
- RFC 5321: Simple Mail Transfer Protocol (SMTP)
- NS-3 Official Documentation: https://www.nsnam.org/
- NS-3 Python API Reference
- Wireshark Official Documentation
- IEEE Standards for Network Performance

## 📖 File Structure

```
Assignment2/
├── Documentation/
│   ├── README.md (this file)
│   ├── ASSIGNMENT_DETAILS.md
│   └── HTTP_SMTP_Protocols.pdf
├── Source Code/
│   └── NS3_Simulation.py
└── Lab Report/
    ├── LAB_REPORT.md
    ├── HTTP_Packet_Analysis.docx
    └── NS3_Implementation.docx
```

---

**Assignment Date**: Spring 2026  
**Submission Status**: ✅ Completed  
**Student**: MD HASIB ULLAH KHAN ALVIE (22101371)  
**Instructor**: MSMA and SRJ (Lab Faculty)  
**Course**: CSE421 - Networking Protocols and Interconnection  
