# Static Routing Task 2: Configuring Floating Static Routes

## Overview
Floating static routes implement automatic failover by using administrative distance (AD) to designate primary and backup routes. When the primary route becomes unavailable, the backup route automatically activates without manual intervention.

## Objectives
- Understand administrative distance concept
- Configure primary and backup default routes
- Implement automatic route failover
- Test failover and failback scenarios
- Compare static failover vs. dynamic routing
- Understand IPv4 and IPv6 floating routes

## What Are Floating Routes?

### Definition
Floating routes are **backup static routes with a higher administrative distance** than the primary route. They remain inactive (not in routing table) while the primary route is available, but automatically activate when the primary route fails.

### Key Concept: Administrative Distance (AD)
Administrative Distance is a number (0-255) that indicates router **trust level** in a route source:
- **Lower AD = Higher trust = Preferred**
- **Higher AD = Lower trust = Backup**

| Source | Default AD | Use Case |
|--------|-----------|----------|
| Connected interface | 0 | Direct connections (highest trust) |
| Static route | 1 | Manually configured routes |
| EIGRP | 90 | Advanced dynamic routing |
| OSPF | 110 | Standard dynamic routing |
| RIP | 120 | Basic dynamic routing |
| Unusable | 255 | Never used |

### Why Use Floating Routes?
```
Scenario: ISP Link Redundancy

Primary Route (AD 1):
ip route 0.0.0.0 0.0.0.0 192.168.1.1
↑ Active route - all traffic through ISP A

Backup Route (AD 5):
ip route 0.0.0.0 0.0.0.0 192.168.2.1 5
↑ Inactive - in configuration but not used

When ISP A (192.168.1.1) becomes unavailable:
- Primary route disappears
- Backup route (AD 5) automatically activates
- Traffic switches to ISP B (192.168.2.1)
- No manual intervention needed!
```

## Network Topology

### Edge Router Configuration
```
Edge Router
├── Serial 0/0/0 → ISP A (Primary)
│   └── Default route: AD 1
├── Serial 0/0/1 → ISP B (Backup)
│   └── Default route: AD 5 (Floating)
└── G0/0 → Internal Network (172.31.1.0/24)
```

## Configuration

### Primary Default Route
```
ip route 0.0.0.0 0.0.0.0 s0/0/0
```
- Destination: 0.0.0.0/0 (all networks - catch-all)
- Next-hop: Serial 0/0/0 interface
- AD: 1 (default for static routes)
- Status: **ACTIVE** (preferred route)

### Backup Floating Route
```
ip route 0.0.0.0 0.0.0.0 s0/0/1 5
```
- Destination: 0.0.0.0/0 (same as primary)
- Next-hop: Serial 0/0/1 interface
- AD: 5 (higher than primary)
- Status: **INACTIVE** (standby)

### IPv6 Floating Routes (Bonus)
```
Primary:   ipv6 route ::/0 2001:DB8:A:1::1
Backup:    ipv6 route ::/0 2001:DB8:A:2::1 5
```

## How Floating Routes Work

### Normal Operation (Primary Active)
```
Router Routing Table:
S   0.0.0.0/0 [1/0] via s0/0/0
    (Backup route NOT shown - hidden by primary)

Routing Decision:
- Check destination IP
- Find matching route: 0.0.0.0/0 (matches everything)
- Use AD 1 primary route
- Forward via s0/0/0
```

### Primary Link Fails (Backup Activates)
```
Timeline:
1. s0/0/0 interface goes DOWN
2. Primary route removed from table
3. AD 1 primary no longer available
4. AD 5 backup becomes best available
5. Backup route activates AUTOMATICALLY

Router Routing Table (After Failure):
S   0.0.0.0/0 [5/0] via s0/0/1
    (Now using backup route)

Routing Decision:
- Check destination IP
- Find matching route: 0.0.0.0/0 (still matches)
- Use AD 5 backup route (now best available)
- Forward via s0/0/1
```

### Primary Link Restored (Failback)
```
Timeline:
1. s0/0/0 interface comes UP
2. Primary route reinstalled
3. AD 1 primary now available again
4. AD 5 backup automatically returns to standby
5. Traffic switches back to primary

Router Routing Table (After Recovery):
S   0.0.0.0/0 [1/0] via s0/0/0
    (Backup route hidden again)

Routing Decision:
- Check destination IP
- Find matching route: 0.0.0.0/0
- Use AD 1 primary route (better than AD 5)
- Forward via s0/0/0
```

## Failover Testing

### Manual Failover Test
```bash
# To simulate primary link failure for testing:
Edge_Router(config)#interface s0/0/0
Edge_Router(config-if)#shutdown

# Observe: Backup route activates immediately
Edge_Router#show ip route

# To restore primary:
Edge_Router(config-if)#no shutdown

# Observe: Primary route becomes active again
Edge_Router#show ip route
```

## Verification Commands

### Display Routing Table
```
show ip route
```
**Output shows**:
- Route destination (0.0.0.0/0)
- Administrative Distance in [brackets]
- Active next-hop interface

### Display Static Routes Only
```
show ip route static
```

### Display Specific Route Details
```
show ip route 0.0.0.0
```

### Check Interface Status
```
show interface s0/0/0
show interface s0/0/1
show interface serial 0/0/0 brief
```

### View Running Configuration
```
show running-config | include route
```

### Test Route with Ping
```
ping 8.8.8.8
traceroute 8.8.8.8
```

## Advantages of Floating Routes

| Advantage | Benefit |
|-----------|---------|
| **Automatic Failover** | No manual intervention needed |
| **Simple Configuration** | Easy to understand and deploy |
| **Predictable Paths** | Control exact failover routes |
| **Cost Optimization** | Use expensive link only when needed |
| **No Protocol Overhead** | No continuous routing updates |
| **Fast Failover** | Immediate route activation |

## Disadvantages of Floating Routes

| Disadvantage | Impact |
|----------|---------
| **Manual Detection** | Must detect failure by interface down |
| **No Load Balancing** | Only one route active at a time |
| **Limited Scalability** | Complex with many routes |
| **No Optimization** | Can't select best path dynamically |
| **Convergence Issues** | Depends on interface down detection |

## Comparison: Floating Routes vs Alternatives

### Floating Static Routes
- Primary and backup with different ADs
- Automatic failover
- Simple configuration
- No protocol overhead

### Dynamic Routing (RIPv2, OSPF, EIGRP)
- Automatic route discovery
- Multiple paths analyzed
- Automatic failover
- Complex configuration
- Continuous protocol overhead

### Manual Failover
- Administrator manually changes routes
- No automation
- Error-prone
- Slower failover

### Hot Standby Routing Protocol (HSRP)
- Virtual IP address for gateway
- Layer 3 redundancy
- Very fast failover
- More complex setup

## Real-World Use Cases

### 1. ISP Redundancy
```
Primary: Default route via ISP A (AD 1)
Backup: Default route via ISP B (AD 5)

Benefit: Continue internet access if ISP A fails
Cost: Pay for backup only when needed
```

### 2. Data Center Failover
```
Primary: Route to main datacenter (AD 1)
Backup: Route to disaster recovery site (AD 5)

Benefit: Automatic failover if main DC unavailable
Result: Service continuity with minimal downtime
```

### 3. WAN Optimization
```
Primary: Fast, expensive satellite link (AD 1)
Backup: Slow, cheap dial-up link (AD 5)

Benefit: Use expensive link normally, cheap link on failure
Savings: Reduced WAN costs
```

### 4. Multi-Branch Networks
```
Each branch has floating routes:
Primary: Direct to headquarters
Backup: Through intermediate branch

Benefit: Load distribution and redundancy
Result: Resilient network with cost optimization
```

## Configuration Best Practices

### 1. Administrative Distance Selection
```
Primary: AD 1 (default - highest trust)
Backup: AD 5-10 (distinctly higher)
Never use AD 0 (reserved for connected routes)
```

### 2. Route Uniqueness
```
✅ Recommended:
ip route 0.0.0.0 0.0.0.0 s0/0/0
ip route 0.0.0.0 0.0.0.0 s0/0/1 5

❌ Wrong (both same AD - load balance):
ip route 0.0.0.0 0.0.0.0 s0/0/0
ip route 0.0.0.0 0.0.0.0 s0/0/1 (AD defaults to 1)
```

### 3. Interface vs. IP Next-Hop
```
Interface-based (recommended):
ip route 0.0.0.0 0.0.0.0 s0/0/0

IP-based:
ip route 0.0.0.0 0.0.0.0 192.168.1.1

Use interface-based for point-to-point links
```

### 4. Documentation
```
Maintain detailed documentation:
- Route purpose (primary/backup)
- Next-hop devices
- Administrative distance values
- Failover scenarios
- Testing procedures
```

## Troubleshooting

### Problem: Backup Route Not Activating
```
Check: show running-config | include route
Verify: Backup AD > Primary AD
Confirm: Primary interface actually failed
Monitor: debug ip routing
```

### Problem: Both Routes Active
```
Cause: Same AD value for both routes
Fix: Ensure backup has HIGHER AD
Check: show ip route (look for multiple paths)
```

### Problem: Failover Delay
```
Cause: Interface convergence time
Solution: Link down detection delay
Result: Typically 1-3 seconds
Speed Up: Use BFD (Bidirectional Forwarding Detection)
```

### Problem: Route Not Installing
```
Check: ip route syntax correctness
Verify: Next-hop interface exists
Ensure: Interface has IP configured
Confirm: No conflicting routes
```

## Learning Outcomes

After completing this task, you should understand:
- Administrative distance and route preference
- Floating route configuration and operation
- Automatic failover mechanisms
- Primary and backup route selection
- Failover testing and verification
- Real-world redundancy scenarios
- Limitations and best practices
- Comparison with dynamic routing

## Advanced Topics

### IPv6 Floating Routes
Same concept for IPv6:
```
ipv6 route ::/0 2001:DB8:A:1::1
ipv6 route ::/0 2001:DB8:A:2::1 5
```

### Multiple Backup Routes
```
Primary (AD 1):    ip route 0.0.0.0 0.0.0.0 s0/0/0
Backup 1 (AD 5):   ip route 0.0.0.0 0.0.0.0 s0/0/1 5
Backup 2 (AD 10):  ip route 0.0.0.0 0.0.0.0 s0/0/2 10
```

### Combining with Dynamic Routing
```
Static floating routes for known paths
Dynamic routing for discovery of new paths
Best of both worlds approach
```

---
**Completed By**: MD HASIB ULLAH KHAN ALVIE
**Student ID**: 22101371
**Course**: CSE421
**Lab Faculty**: MSMA, SRJ
**University**: BRAC University
**Semester**: Spring26
