# Static Routing Task 1: Configuring IPv4 Static and Default Routes

## Overview
This task demonstrates manual route configuration on Cisco routers using static routes. Unlike dynamic routing (learned automatically), static routes require manual specification of network paths and are commonly used in small networks or as backup routes.

## Objectives
- Configure static routes on multiple routers
- Understand manual route configuration
- Implement default routes for edge devices
- Test connectivity across configured routes
- Compare static vs. dynamic routing approaches

## Network Topology

### Network Segments
```
R1 LAN          R1-to-R2       R2-to-R3 Seg1   R2-to-R3 Seg2   R3-Link
172.31.0.0/24   172.31.1.0/25  172.31.1.0/25   172.31.1.128/26 172.31.1.196/30
```

### Router Connections
| Router | Connected Networks | Next Hops |
|--------|-------------------|-----------|
| **R1** | 172.31.0.0/24 | Gateway: 172.31.1.193 |
| **R2** | 172.31.1.0/25 (se0/0/0), 172.31.1.128/26 (se0/0/1) | Interface-based |
| **R3** | 172.31.1.196/30 (se0/0/1) | Default route to se0/0/1 |

## Static Route Configuration

### R1 Configuration
```
ip route 172.31.0.0 255.255.255.0 172.31.1.193
ip route 172.31.1.128 255.255.255.192 172.31.1.193
ip route 172.31.1.196 255.255.255.252 172.31.1.193
```

**Explanation**:
- Destination network 172.31.0.0 with mask 255.255.255.0
- Via next-hop gateway 172.31.1.193
- Three separate routes for three network destinations

### R2 Configuration
```
ip route 172.31.1.0 255.255.255.128 se0/0/0
ip route 172.31.1.128 255.255.255.192 se0/0/1
```

**Explanation**:
- Routes via specific serial interfaces
- Interface-based next-hop instead of IP address
- Connects to two different network segments

### R3 Configuration
```
ip route 0.0.0.0 0.0.0.0 se0/0/1
```

**Explanation**:
- Default route (0.0.0.0/0 = all networks)
- All unknown traffic directed to se0/0/1
- Typical configuration for edge/remote routers

## Static Route Syntax

### Command Format
```
ip route <destination-network> <subnet-mask> <next-hop>
```

### Examples
| Example | Meaning |
|---------|---------|
| `ip route 172.31.0.0 255.255.255.0 172.31.1.193` | Route to 172.31.0.0/24 via IP 172.31.1.193 |
| `ip route 172.31.1.0 255.255.255.128 se0/0/0` | Route to 172.31.1.0/25 via interface se0/0/0 |
| `ip route 0.0.0.0 0.0.0.0 se0/0/1` | Default route - all unknown destinations |

### Next-Hop Types
1. **IP Address**: `ip route 10.0.0.0 255.255.255.0 192.168.1.1`
2. **Interface**: `ip route 10.0.0.0 255.255.255.0 Serial0/0/0`
3. **Interface + IP**: `ip route 10.0.0.0 255.255.255.0 Serial0/0/0 192.168.1.1`

## Default Routes

### What is a Default Route?
- Network: 0.0.0.0 with mask 0.0.0.0 (meaning ALL networks)
- Used when no more specific route exists
- Commonly used on edge routers
- Reduces routing table size

### Default Route Example
```
ip route 0.0.0.0 0.0.0.0 se0/0/1
```

This means: "For any destination not in my routing table, send it out se0/0/1"

### Use Cases
- **Edge routers** pointing to ISP
- **Branch offices** with single WAN connection
- **End-of-line devices** with no further routes
- **Backup routes** for unspecified destinations

## Verification Commands

### View Routing Table
```
show ip route
```

**Output includes**:
- Route destination and mask
- Administrative distance and metric
- Next-hop address or interface
- Route source (S = Static)

### Check Route Details
```
show ip route static
```
Shows only static routes (S denotes static in main table)

### Test Connectivity
```
ping <destination-ip>
traceroute <destination-ip>
```

### Debug Routing
```
debug ip routing
show ip route <destination>
```

## Connectivity Tests

### PC1 Tests
```
ping 172.31.0.254    # Gateway test
ping 172.31.1.190    # R2 network test
```

### PC2 Tests
```
ping 172.31.1.126    # R2-R3 segment test
ping 172.31.1.190    # R2 reachability
```

### PC3 Tests
```
ping 172.31.0.254    # R1 LAN test
ping 172.31.1.126    # R3 network test
```

## Advantages of Static Routing

| Advantage | Benefit |
|-----------|---------|
| **Control** | Administrator chooses exact paths |
| **Predictability** | Routes don't change unexpectedly |
| **Efficiency** | No overhead of routing protocol |
| **Security** | No dynamic protocol traffic to monitor |
| **Simplicity** | Easy to understand for small networks |

## Limitations of Static Routing

| Limitation | Impact |
|-----------|--------|
| **Scalability** | Manual config for each route |
| **Failover** | No automatic alternate routes |
| **Maintenance** | Must update manually on changes |
| **Growth** | Difficult in large networks |
| **Efficiency** | Not optimal path selection |

## Comparison: Static vs Dynamic vs Default Routes

| Feature | Static | Dynamic (RIPv2) | Default |
|---------|--------|-----------------|---------|
| **Config** | Manual | Automatic | Manual (often static) |
| **Update** | Manual | Automatic | Static |
| **Failover** | Manual | Automatic | No failover |
| **Best for** | Small/specific | Medium networks | Edge/unknown |
| **Overhead** | None | Periodic updates | Minimal |

## Real-World Applications

### Scenario 1: Small Office Network
```
Branch office has one WAN link to headquarters
Use static routes: one default route to HQ router
All traffic destined for HQ sent via WAN link
```

### Scenario 2: Multi-Router Core Network
```
Three routers in controlled environment
Each route manually configured
Paths designed for specific security/performance
No dynamic protocol overhead
```

### Scenario 3: Mixed Environment
```
Static routes for known, stable paths
Default route as catch-all
Backup routes with different cost (Floating routes - Task 2)
```

## When to Use Static Routing

✅ **Use Static Routes When:**
- Network is small (< 5 routers)
- Topology is stable and simple
- Specific path control needed
- Security requires predictable behavior
- No dynamic routing protocol available

❌ **Don't Use Static Routes When:**
- Network is large (> 20 routers)
- Topology changes frequently
- Automatic failover needed
- Redundancy important
- Network growth expected

## Troubleshooting Guide

### Routes Not Installing
```
Check: ip route syntax
Verify: Next-hop is reachable
Ensure: Source interface is up/up
```

### Ping Fails
```
Check: Routes on both directions
Verify: Return path exists
Confirm: No firewalls blocking
Test: Traceroute to verify path
```

### Wrong Route Selected
```
Check: Administrative distance values
Verify: Route specificity (longest match)
Review: Multiple route entries
Use: Show ip route <destination>
```

## Learning Outcomes

After this task, you should understand:
- Manual static route configuration
- When to use static vs. dynamic routing
- Default route concepts and usage
- Route verification procedures
- Troubleshooting routing issues
- Static routing design patterns

---
**Completed By**: MD HASIB ULLAH KHAN ALVIE
**Student ID**: 22101371
**Course**: CSE421
**Lab Faculty**: MSMA, SRJ
**University**: BRAC University
**Semester**: Spring26
