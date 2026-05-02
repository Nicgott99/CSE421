# Assignment 2: Detailed Implementation Guide

## Protocol Analysis: HTTP and SMTP

### HTTP (HyperText Transfer Protocol)

#### HTTP Request Structure
```
METHOD /path HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
Content-Length: 348
Content-Type: application/x-www-form-urlencoded

[Request Body - if applicable]
```

#### HTTP Methods
- **GET**: Retrieve resource from server
- **POST**: Submit data to server
- **PUT**: Update existing resource
- **DELETE**: Remove resource
- **HEAD**: Like GET but without response body
- **OPTIONS**: Describe communication options

#### HTTP Status Codes
| Code | Meaning | Category |
|------|---------|----------|
| 200 | OK | Success |
| 201 | Created | Success |
| 304 | Not Modified | Redirection |
| 400 | Bad Request | Client Error |
| 401 | Unauthorized | Client Error |
| 404 | Not Found | Client Error |
| 500 | Server Error | Server Error |
| 503 | Service Unavailable | Server Error |

#### HTTP Response Structure
```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1234
Server: Apache/2.4.41
Date: Thu, 03 May 2026 10:30:00 GMT

[Response Body]
```

### SMTP (Simple Mail Transfer Protocol)

#### SMTP Communication Flow

```
1. Client connects to server (port 25, 587, or 465)
   Client → Server: TCP connection established
   Server → Client: 220 mail.example.com ESMTP

2. Client initiates conversation
   Client → Server: EHLO client.example.com
   Server → Client: 250-mail.example.com offers these SMTP features

3. Email submission
   Client → Server: MAIL FROM:<sender@example.com>
   Server → Client: 250 OK

4. Recipient specification
   Client → Server: RCPT TO:<recipient@example.com>
   Server → Client: 250 OK

5. Message body
   Client → Server: DATA
   Server → Client: 354 Start mail input
   Client → Server: [Email headers and body]
   Client → Server: .
   Server → Client: 250 OK

6. Session termination
   Client → Server: QUIT
   Server → Client: 221 Bye
```

#### SMTP Commands and Responses

| Command | Purpose | Example Response |
|---------|---------|------------------|
| HELO/EHLO | Identify client | 250 Server ready |
| MAIL FROM | Specify sender | 250 OK |
| RCPT TO | Specify recipient | 250 OK |
| DATA | Begin message body | 354 Start input |
| VRFY | Verify address | 250 Verified |
| EXPN | Expand mailing list | 250 List expanded |
| QUIT | Close connection | 221 Bye |

---

## Network Simulation: NS-3 Implementation

### NS-3 Architecture Overview

NS-3 (Network Simulator 3) is a discrete-event network simulator designed for research and educational purposes.

#### Key Components

1. **Core Module**
   - Event scheduling
   - Time management
   - Logging and tracing

2. **Network Module**
   - Node and device models
   - Channel models
   - PHY layer simulation

3. **Internet Module**
   - TCP/IP stack implementation
   - IPv4 and IPv6 support
   - Routing protocols

4. **Application Module**
   - Application layer models
   - UDP/TCP applications
   - Built-in application helpers

5. **Flow Monitor**
   - Network performance metrics
   - Flow statistics collection
   - Classifier for flow identification

### Simulation Workflow

#### Step 1: Create Network Nodes
```python
nodes = ns.network.NodeContainer()
nodes.Create(2)  # Create 2 nodes
```
- Creates Node 0 and Node 1
- Nodes are bare containers for network stack

#### Step 2: Create Links Between Nodes
```python
pointToPoint = ns.point_to_point.PointToPointHelper()
pointToPoint.SetDeviceAttribute("DataRate", ns.core.StringValue("5Mbps"))
pointToPoint.SetChannelAttribute("Delay", ns.core.StringValue("2ms"))
devices = pointToPoint.Install(nodes)
```
- Creates point-to-point link
- Sets data rate to 5 Mbps
- Sets link delay to 2 ms

#### Step 3: Install Internet Stack
```python
stack = ns.internet.InternetStackHelper()
stack.Install(nodes)
```
- Installs TCP/IP stack on all nodes
- Enables routing capabilities

#### Step 4: Assign IP Addresses
```python
address = ns.internet.Ipv4AddressHelper()
address.SetBase(ns.network.Ipv4Address("10.1.1.0"),
                ns.network.Ipv4Mask("255.255.255.0"))
interfaces = address.Assign(devices)
```
- Sets IP address base: 10.1.1.0/24
- Assigns sequential IPs to interfaces

#### Step 5: Create Applications
```python
# Server
echoServer = ns.applications.UdpEchoServerHelper(9)
serverApps = echoServer.Install(nodes.Get(1))
serverApps.Start(ns.core.Seconds(1.0))
serverApps.Stop(ns.core.Seconds(10.0))

# Client
echoClient = ns.applications.UdpEchoClientHelper(address, 9)
clientApps = echoClient.Install(nodes.Get(0))
clientApps.Start(ns.core.Seconds(2.0))
clientApps.Stop(ns.core.Seconds(10.0))
```
- UDP Echo Server on Node 1, port 9
- UDP Echo Client on Node 0
- Server runs 1-10 seconds
- Client runs 2-10 seconds

#### Step 6: Enable Flow Monitoring
```python
flowmon_helper = ns.flow_monitor.FlowMonitorHelper()
monitor = flowmon_helper.InstallAll()
```
- Installs flow monitor on all devices
- Captures network statistics

#### Step 7: Run Simulation
```python
ns.core.Simulator.Stop(ns.core.Seconds(20.0))
ns.core.Simulator.Run()
```
- Simulation runs until 20 seconds
- Processes all scheduled events

#### Step 8: Collect Statistics
```python
for flow_id, flow_stats in monitor.GetFlowStats():
    # Process flow statistics
    print("Tx Bytes: ", flow_stats.txBytes)
    print("Rx Bytes: ", flow_stats.rxBytes)
    print("Tx Packets: ", flow_stats.txPackets)
    print("Rx Packets: ", flow_stats.rxPackets)
    print("Lost Packets: ", flow_stats.lostPackets)
```
- Iterates through all flows
- Retrieves and prints performance metrics

---

## Performance Metrics Interpretation

### Throughput Calculation

**Formula**: Throughput = (Received Bytes × 8) / Duration (in bits)

Example:
- Received: 2048 bytes
- Duration: 18 seconds
- Throughput = (2048 × 8) / 18 = 910.22 bits/second ≈ 0.91 kbps

### Latency Measurement

**Mean Delay**: Sum of all delays / Number of received packets

Example:
- Delay sum: 36 ms
- Packets received: 1
- Mean delay = 36 / 1 = 36 ms

### Packet Loss Calculation

**Packet Loss Ratio**: (Lost Packets / Transmitted Packets) × 100%

Example:
- Transmitted: 1 packet
- Lost: 0 packets
- Loss ratio = 0%

### Interpretation Guidelines

| Metric | Good Range | Warning | Critical |
|--------|-----------|---------|----------|
| Throughput | > 80% of link | 50-80% | < 50% |
| Mean Delay | < 50 ms | 50-200 ms | > 200 ms |
| Packet Loss | 0-1% | 1-5% | > 5% |

---

## Expected Simulation Output

```
FlowID: 1 (UDP 10.1.1.1/1234 --> 10.1.1.2/9)
Tx Bytes: 2048
Rx Bytes: 2048
Tx Packets: 1
Rx Packets: 1
Lost Packets: 0
Mean Delay: 0.004 seconds (4 ms)
Throughput: 910.22 bits/second
```

---

## Advanced Topics

### Flow Classification
- Source address, destination address
- Source port, destination port
- Protocol type (TCP/UDP)
- Unique flow identification

### Multi-Flow Simulation
- Multiple simultaneous flows
- Congestion scenarios
- Competing traffic analysis

### Channel Impairments
- Packet loss models
- Error models
- Queuing disciplines

### Routing Protocols
- Static routing
- Dynamic routing (RIP, OSPF, EIGRP)
- Protocol simulation and comparison

---

**Created**: May 2026  
**Course**: CSE421 - Networking Protocols and Interconnection  
**Lab Faculty**: MSMA and SRJ  
