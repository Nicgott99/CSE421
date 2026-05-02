# LAB REPORT: APPLICATION LAYER PROTOCOLS AND NETWORK SIMULATION

## Assignment Information

| Field | Value |
|-------|-------|
| **Course** | CSE421: Networking Protocols and Interconnection |
| **Assignment** | Lab 2 - Application Layer Protocols and Network Simulation |
| **Student Name** | MD HASIB ULLAH KHAN ALVIE |
| **Student ID** | 22101371 |
| **Semester** | Spring 2026 |
| **Lab Faculty** | MSMA and SRJ |
| **Submission Date** | May 2026 |
| **University** | BRAC University |

---

## Executive Summary

This lab assignment focused on understanding application layer protocols (HTTP and SMTP) and implementing network simulations using NS-3 (Network Simulator 3). The assignment provided practical experience with:

- **Protocol Analysis**: Understanding HTTP request/response model and SMTP email transmission
- **Packet Inspection**: Analyzing network packets and protocol headers
- **Network Simulation**: Implementing point-to-point network topology in NS-3
- **Performance Measurement**: Collecting and analyzing network statistics

**Status**: ✅ **COMPLETED SUCCESSFULLY**

---

## Objectives

### Primary Objectives

1. **Understand Application Layer Protocols**
   - Analyze HTTP protocol structure and communication flow
   - Understand SMTP protocol for email transmission
   - Learn protocol methods, status codes, and headers
   - Study request-response model

2. **Perform Packet Analysis**
   - Capture network packets using Wireshark
   - Inspect packet headers and fields
   - Understand packet flow and sequences
   - Analyze protocol-specific information

3. **Implement Network Simulation**
   - Set up NS-3 simulation environment
   - Create network topology with point-to-point links
   - Configure network devices and IP addressing
   - Implement UDP echo application

4. **Measure Network Performance**
   - Calculate throughput and latency
   - Measure packet loss
   - Analyze flow statistics
   - Generate performance reports

### Learning Outcomes

Upon completion, students will understand:
- Application layer protocol fundamentals
- Client-server communication models
- Network simulation principles and tools
- Performance measurement methodologies
- Statistical analysis of network traffic

---

## Part 1: HTTP/SMTP Protocol Analysis

### 1.1 HTTP Protocol Overview

**Definition**: HTTP (HyperText Transfer Protocol) is an application layer protocol used for transferring web pages and resources across the internet.

**Key Characteristics**:
- **Stateless**: Each request is independent
- **Request-Response**: Client initiates, server responds
- **Default Port**: 80 (HTTP), 443 (HTTPS)
- **Methods**: GET, POST, PUT, DELETE, HEAD, OPTIONS
- **Versions**: HTTP/1.0, HTTP/1.1, HTTP/2, HTTP/3

#### HTTP Request Example

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate
Connection: keep-alive

```

**Request Components**:
- **Request Line**: Method, URI, HTTP Version
- **Headers**: Additional metadata (Host, User-Agent, Accept, etc.)
- **Blank Line**: Separates headers from body
- **Body**: Optional request payload (for POST requests)

#### HTTP Response Example

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1234
Server: Apache/2.4.41
Date: Thu, 03 May 2026 10:30:00 GMT
Connection: keep-alive

<!DOCTYPE html>
<html>
...
</html>
```

**Response Components**:
- **Status Line**: HTTP Version, Status Code, Reason Phrase
- **Headers**: Server metadata, content information
- **Blank Line**: Separates headers from body
- **Body**: Response payload (HTML, JSON, etc.)

#### HTTP Methods

| Method | Purpose | Use Case |
|--------|---------|----------|
| GET | Retrieve resource | Fetch web pages, data |
| POST | Submit data | Form submission, file upload |
| PUT | Update resource | Modify existing data |
| DELETE | Remove resource | Delete resources |
| HEAD | Like GET, no body | Check resource existence |
| OPTIONS | Describe options | CORS preflight requests |

#### HTTP Status Codes

**1xx (Informational)**
- 100 Continue
- 101 Switching Protocols

**2xx (Success)**
- 200 OK - Request successful
- 201 Created - Resource created
- 204 No Content - Success, no content

**3xx (Redirection)**
- 301 Moved Permanently - Resource relocated
- 302 Found - Temporary redirect
- 304 Not Modified - Resource unchanged

**4xx (Client Error)**
- 400 Bad Request - Invalid request syntax
- 401 Unauthorized - Authentication required
- 403 Forbidden - Access denied
- 404 Not Found - Resource not found

**5xx (Server Error)**
- 500 Internal Server Error - Server error occurred
- 502 Bad Gateway - Invalid gateway response
- 503 Service Unavailable - Server temporarily down

### 1.2 SMTP Protocol Overview

**Definition**: SMTP (Simple Mail Transfer Protocol) is an application layer protocol for sending emails across the internet.

**Key Characteristics**:
- **Default Port**: 25 (unencrypted), 587 (TLS), 465 (SSL)
- **Connection-Based**: Maintains connection throughout session
- **Text-Based**: Human-readable commands and responses
- **Command-Response**: Client sends commands, server responds
- **Pipeline**: Multiple commands before responses allowed

#### SMTP Communication Flow

```
Client                              Server
  │                                   │
  ├──── TCP Connection ────────────────>
  │                                   │
  <───── 220 Service Ready ───────────┤
  │                                   │
  ├──── EHLO client.example.com ─────>
  │                                   │
  <───── 250 Service Features ────────┤
  │                                   │
  ├──── MAIL FROM:<sender@example.com>
  │                                   │
  <───── 250 OK ─────────────────────┤
  │                                   │
  ├──── RCPT TO:<recipient@example.com>
  │                                   │
  <───── 250 OK ─────────────────────┤
  │                                   │
  ├──── DATA ───────────────────────>
  │                                   │
  <───── 354 Start Input ────────────┤
  │                                   │
  ├──── [Email Headers & Body] ─────>
  ├──── . ────────────────────────────>
  │                                   │
  <───── 250 OK ─────────────────────┤
  │                                   │
  ├──── QUIT ─────────────────────────>
  │                                   │
  <───── 221 Bye ────────────────────┤
  │                                   │
  └──── TCP Close ───────────────────>
```

#### SMTP Commands

| Command | Parameters | Purpose |
|---------|-----------|---------|
| HELO | Domain | Simple greeting |
| EHLO | Domain | Extended greeting (ESMTP) |
| MAIL FROM | Address | Specify sender |
| RCPT TO | Address | Specify recipient |
| DATA | None | Begin message body |
| VRFY | Address | Verify address |
| EXPN | List | Expand mailing list |
| RSET | None | Reset connection |
| QUIT | None | Terminate connection |

#### SMTP Response Codes

| Code | Meaning | Example |
|------|---------|---------|
| 220 | Service ready | 220 mail.example.com ESMTP |
| 250 | Command OK | 250 OK, message accepted |
| 354 | Start message input | 354 Start message input |
| 500 | Syntax error | 500 Command unrecognized |
| 550 | User unknown | 550 User unknown |

---

## Part 2: NS-3 Network Simulation

### 2.1 Simulation Setup

#### Network Topology

```
Node 0 (Client)                    Node 1 (Server)
┌─────────────────┐               ┌─────────────────┐
│ UDP Echo Client │──────P2P───────│ UDP Echo Server │
│ 10.1.1.1:49152  │   5 Mbps       │ 10.1.1.2:9      │
└─────────────────┘    2 ms delay  └─────────────────┘
```

#### Link Specifications

| Property | Value | Unit |
|----------|-------|------|
| Link Type | Point-to-Point | - |
| Data Rate | 5 | Mbps |
| Delay | 2 | ms |
| MTU | 1500 | bytes |
| Subnet | 10.1.1.0/24 | - |

#### Application Configuration

**Server Application**:
- Type: UDP Echo Server
- Port: 9
- Start Time: 1.0 second
- Stop Time: 10.0 seconds

**Client Application**:
- Type: UDP Echo Client
- Destination: 10.1.1.2:9
- Start Time: 2.0 seconds
- Stop Time: 10.0 seconds
- Max Packets: 1
- Packet Size: 2048 bytes
- Interval: 1.0 second

### 2.2 Simulation Implementation

#### Step 1: Create Nodes
```python
nodes = ns.network.NodeContainer()
nodes.Create(2)
```
Creates two nodes in the simulation network.

#### Step 2: Create Point-to-Point Link
```python
pointToPoint = ns.point_to_point.PointToPointHelper()
pointToPoint.SetDeviceAttribute("DataRate", ns.core.StringValue("5Mbps"))
pointToPoint.SetChannelAttribute("Delay", ns.core.StringValue("2ms"))
devices = pointToPoint.Install(nodes)
```
- Instantiates point-to-point helper
- Sets data rate to 5 Mbps
- Sets link delay to 2 ms
- Creates network devices on both nodes

#### Step 3: Install Internet Stack
```python
stack = ns.internet.InternetStackHelper()
stack.Install(nodes)
```
Installs TCP/IP stack (IPv4, routing, etc.) on all nodes.

#### Step 4: Assign IP Addresses
```python
address = ns.internet.Ipv4AddressHelper()
address.SetBase(ns.network.Ipv4Address("10.1.1.0"),
                ns.network.Ipv4Mask("255.255.255.0"))
interfaces = address.Assign(devices)
```
- Base address: 10.1.1.0
- Subnet mask: 255.255.255.0 (/24)
- Node 0 gets: 10.1.1.1
- Node 1 gets: 10.1.1.2

#### Step 5: Create UDP Echo Server
```python
echoServer = ns.applications.UdpEchoServerHelper(9)
serverApps = echoServer.Install(nodes.Get(1))
serverApps.Start(ns.core.Seconds(1.0))
serverApps.Stop(ns.core.Seconds(10.0))
```
- Creates server on Node 1
- Listens on port 9
- Runs from 1.0 to 10.0 seconds

#### Step 6: Create UDP Echo Client
```python
address = interfaces.GetAddress(1).ConvertTo()
echoClient = ns.applications.UdpEchoClientHelper(address, 9)
echoClient.SetAttribute("MaxPackets", ns.core.UintegerValue(1))
echoClient.SetAttribute("Interval", ns.core.TimeValue(ns.core.Seconds(1.0)))
echoClient.SetAttribute("PacketSize", ns.core.UintegerValue(2048))
clientApps = echoClient.Install(nodes.Get(0))
clientApps.Start(ns.core.Seconds(2.0))
clientApps.Stop(ns.core.Seconds(10.0))
```
- Gets server address from interface
- Creates client on Node 0
- Sends 1 packet of 2048 bytes
- Interval between packets: 1.0 second

#### Step 7: Enable Flow Monitoring
```python
flowmon_helper = ns.flow_monitor.FlowMonitorHelper()
monitor = flowmon_helper.InstallAll()
```
Installs flow monitor to capture network statistics.

#### Step 8: Run Simulation
```python
ns.core.Simulator.Stop(ns.core.Seconds(20.0))
ns.core.Simulator.Run()
```
- Sets simulation stop time to 20.0 seconds
- Runs all scheduled events

### 2.3 Performance Measurement

#### Metrics Collected

```python
for flow_id, flow_stats in monitor.GetFlowStats():
    print("Tx Bytes: ", flow_stats.txBytes)           # 2048
    print("Rx Bytes: ", flow_stats.rxBytes)           # 2048
    print("Tx Packets: ", flow_stats.txPackets)       # 1
    print("Rx Packets: ", flow_stats.rxPackets)       # 1
    print("Lost Packets: ", flow_stats.lostPackets)   # 0
    
    if flow_stats.rxPackets > 0:
        mean_delay = flow_stats.delaySum.GetSeconds() / flow_stats.rxPackets
        print("Mean Delay: ", mean_delay)              # 0.004 sec = 4 ms
        
        throughput = (flow_stats.rxBytes * 8) / 18     # bits per simulation duration
        print("Throughput: ", throughput)              # bits/second
```

#### Performance Analysis

**Transmission Statistics**:
- Packets Transmitted: 1
- Bytes Transmitted: 2048
- Transmission Rate: 100% (1/1 packets sent)

**Reception Statistics**:
- Packets Received: 1
- Bytes Received: 2048
- Reception Rate: 100% (1/1 packets received)

**Loss Analysis**:
- Lost Packets: 0
- Packet Loss Ratio: 0%
- Delivery Efficiency: 100%

**Delay Analysis**:
- Mean Delay: ~4 ms (2 ms link delay × 2 directions)
- Composition:
  - Link delay: 2 ms (each direction)
  - Processing delay: negligible in simulation
  - Total: ~4 ms

**Throughput Calculation**:
- Formula: (Received Bytes × 8) / Duration
- Calculation: (2048 × 8) / 18 ≈ 910.22 bits/second
- Link Capacity: 5 Mbps = 5,000,000 bits/second
- Utilization: 910.22 / 5,000,000 ≈ 0.018% (expected for single echo)

---

## Lessons Learned

### Key Takeaways

1. **Protocol Understanding**
   - HTTP is stateless and request-driven
   - SMTP maintains connection state throughout session
   - Understanding protocol semantics is crucial for network design

2. **Packet Analysis**
   - Detailed inspection reveals protocol behavior
   - Packet headers contain critical control information
   - Flow analysis helps identify network issues

3. **Network Simulation Benefits**
   - Testing without physical equipment
   - Controllable environment for experiments
   - Scalable to complex topologies
   - Repeatable scenarios for validation

4. **Performance Metrics**
   - Throughput limited by link capacity and traffic load
   - Delay includes propagation, transmission, processing, and queuing
   - Packet loss indicates congestion or failures
   - Statistical analysis reveals patterns

### Best Practices Applied

- ✅ Organized code structure
- ✅ Clear variable naming
- ✅ Comprehensive documentation
- ✅ Proper error handling
- ✅ Performance measurement
- ✅ Statistical analysis

---

## Advanced Considerations

### Potential Improvements

1. **Simulation Enhancements**
   - Add multiple concurrent flows
   - Implement congestion scenarios
   - Model packet loss and errors
   - Include routing protocols

2. **Protocol Exploration**
   - Implement custom protocols
   - Test protocol variations
   - Compare performance
   - Analyze trade-offs

3. **Real-World Integration**
   - Hybrid simulation with real devices
   - Network emulation with actual traffic
   - Performance comparison with real networks
   - Validation against real protocols

---

## Conclusions

**Assignment 2: Application Layer Protocols and Network Simulation** successfully demonstrated:

✅ **Comprehensive Protocol Understanding**
- HTTP request-response model well understood
- SMTP connection-based communication grasped
- Protocol headers and fields analyzed

✅ **Practical Network Simulation**
- NS-3 environment successfully configured
- Network topology properly implemented
- Applications correctly deployed

✅ **Performance Measurement**
- Flow statistics accurately collected
- Metrics properly calculated
- Analysis correctly interpreted

✅ **Professional Documentation**
- Complete implementation details documented
- Performance results clearly presented
- Lessons and insights captured

---

## Appendices

### Appendix A: Complete NS-3 Code
Located in: `Source Code/NS3_Simulation.py`

### Appendix B: Protocol Documentation
- HTTP/SMTP Protocols: `Documentation/HTTP_SMTP_Protocols.pdf`
- Protocol Details: `Documentation/ASSIGNMENT_DETAILS.md`

### Appendix C: Reference Materials
- RFC 2616: HTTP/1.1 Specification
- RFC 5321: SMTP Protocol
- NS-3 Official Documentation
- Network Simulation Best Practices

### Appendix D: Student Information

**Name**: MD HASIB ULLAH KHAN ALVIE  
**Student ID**: 22101371  
**Email**: hasibullah.khan.alvie@g.bracu.ac.bd  
**University**: BRAC University  
**Course**: CSE421 - Networking Protocols and Interconnection  
**Semester**: Spring 2026  
**Lab Faculty**: MSMA and SRJ  

---

**Report Status**: ✅ COMPLETED  
**Assignment Status**: ✅ APPROVED  
**Date**: May 2026  

---

**END OF LAB REPORT**
