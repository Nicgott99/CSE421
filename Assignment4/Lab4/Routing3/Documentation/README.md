# Routing Task 3: Configuring RIPv2 (Routing Information Protocol)

## Overview
This task covers the configuration of RIPv2 (Routing Information Protocol version 2), a dynamic routing protocol that enables automatic route discovery and advertisement across multiple routers.

## Objectives
- Understand dynamic routing principles
- Configure RIPv2 on multiple routers
- Enable automatic route discovery
- Implement network scalability
- Test inter-router connectivity

## Network Topology

### Router Configuration
```
R1 (Gateway Router)
├─ Networks: 192.168.1.0/24, 192.168.2.0/24
├─ Default Route: via s0/0/1
└─ Passive Interface: g0/0

R2 (Core Router)
├─ Networks: 192.168.2.0/24, 192.168.3.0/24, 192.168.4.0/24
└─ Passive Interface: g0/0

R3 (Edge Router)
├─ Networks: 192.168.1.0/24, 192.168.4.0/24, 192.168.5.0/24
└─ Passive Interface: g0/0
```

### Inter-Router Links
| Link | Network | Purpose |
|------|---------|---------|
| R1-R2 | 192.168.2.0/24 | Primary path R1↔R2 |
| R2-R3 | 192.168.4.0/24 | Primary path R2↔R3 |
| R1-R3 | 192.168.1.0/24 | Alternative path/redundancy |

## RIPv2 Features

### Version Comparison
| Feature | RIPv1 | RIPv2 |
|---------|-------|-------|
| **VLSM Support** | ❌ | ✅ |
| **Route Classifying** | Classfull | Classless |
| **Metric** | Hop Count (max 15) | Hop Count (max 15) |
| **Update Frequency** | 30 seconds | 30 seconds |
| **Authentication** | None | MD5 Support |
| **Prefix Masking** | No | Yes |

### Configuration Features Implemented
1. **Version 2**: Enhanced protocol with VLSM support
2. **Network Statements**: Define participating networks
3. **Auto-summary Disabled**: Prevents route aggregation
4. **Default-information Originate**: Propagates default route
5. **Passive Interfaces**: Prevents updates on LANs

## Configuration Details

### Key Commands Explained

```
router rip              # Enable RIP routing daemon
version 2              # Use RIPv2 protocol
network 192.168.1.0   # Include network in RIP updates
no auto-summary       # Disable route summarization
default-information   # Advertise default route
originate            
passive-interface g0/0 # No RIP updates on this interface
```

### Passive Interfaces
Passive interfaces are configured on LAN connections (g0/0) because:
- LANs don't need routing protocol updates
- Reduces unnecessary network traffic
- Improves security
- Prevents external routing exposure

## Routing Process

### Route Discovery
1. **Router Startup**: Routers initialize RIP and send requests
2. **Response Exchange**: Routers send routing tables to neighbors
3. **Route Learning**: Each router learns remote networks
4. **Table Population**: Routing table updated with learned routes
5. **Periodic Updates**: Every 30 seconds, routers exchange updates

### Route Selection
```
Example: R1 to reach 192.168.5.0 (R3's LAN)
- Option 1: R1 → R3 (2 hops via 192.168.1.0)
- Option 2: R1 → R2 → R3 (2 hops via 192.168.2.0, 192.168.4.0)
- Result: Both equal, load-balanced or first learned route
```

## Verification Commands

### Check Route Table
```
show ip route           # View all routes including RIP routes
show ip route rip       # Show only RIP routes
```

### RIP Specific Information
```
show ip protocols       # RIP configuration and status
show ip rip database    # RIP routing database
debug ip rip            # Real-time RIP packet debugging
```

### Network Connectivity
```
ping 192.168.3.0        # Test connectivity to R2's network
traceroute 192.168.5.0  # Trace path to R3's network
```

## Advantages of RIPv2

| Advantage | Benefit |
|-----------|---------|
| **Simplicity** | Easy to configure and understand |
| **Automatic Discovery** | No manual route configuration needed |
| **Redundancy** | Automatic failover to alternate paths |
| **Scalability** | Handles medium-sized networks well |
| **Compatibility** | Works with legacy and modern equipment |

## Limitations of RIPv2

| Limitation | Impact |
|-----------|--------|
| **15-Hop Limit** | Cannot route beyond 15 hops |
| **Bandwidth** | Periodic updates consume bandwidth |
| **Convergence Time** | Takes time to detect topology changes |
| **CPU Usage** | Continuous route calculation overhead |

## Learning Outcomes

After completing this task, you should understand:
- Dynamic routing protocol principles
- RIPv2 configuration and operation
- Network path selection and redundancy
- Passive interface configuration
- Route verification and troubleshooting

## Practical Applications

RIPv2 is commonly used in:
- Small to medium-sized enterprise networks
- Educational and training environments
- Legacy network infrastructure
- Networks requiring simple routing solutions

---
**Completed By**: MD HASIB ULLAH KHAN ALVIE
**Student ID**: 22101371
**Course**: CSE421
**Lab Faculty**: MSMA, SRJ
**University**: BRAC University
**Semester**: Spring26
