# DHCP Task 2: Configuring DHCPv4 Using Dedicated DHCP Server

## Overview
This task demonstrates the configuration of a dedicated DHCP server appliance in a network environment, with DHCP relay agents (routers) forwarding client requests to the central server.

## Objectives
- Configure DHCP relay agents on routers
- Set up IP helper addresses to forward DHCP requests
- Implement centralized DHCP management
- Understand DHCP relay mechanisms across subnets

## Network Topology
- **Dedicated DHCP Server**: 192.168.60.253
- **Router R1**: DHCP Relay Agent
- **Multiple Client Subnets**: Connected through various routers

## Key Configuration

### DHCP Relay on Router R1
```
interface g0/0
  ip helper-address 192.168.60.253
```

This configuration:
- Receives DHCP DISCOVER broadcasts from clients
- Forwards them to the central DHCP server at 192.168.60.253
- Receives DHCP OFFER responses from server
- Relays responses back to requesting clients

## DHCP Relay Agent How It Works

1. **DHCP Client Request**: Client broadcasts DHCP DISCOVER
2. **Relay Reception**: Router receives the broadcast
3. **Request Forwarding**: Router forwards to DHCP server
4. **Server Response**: DHCP server sends DHCP OFFER
5. **Client Delivery**: Router delivers OFFER to client

## Advantages of Centralized DHCP

| Aspect | Benefit |
|--------|---------|
| **Scalability** | Handle multiple subnets with single server |
| **Administration** | Centralized IP pool and lease management |
| **Consistency** | Unified DHCP policies across network |
| **Resource Usage** | Routers don't consume resources running DHCP |
| **Monitoring** | Easier to track and audit DHCP activity |

## Verification

### Check Relay Configuration
```
show ip route
show ip interface g0/0
```

### Monitor DHCP Activity
```
debug ip udp
show dhcp bindings
show dhcp statistics
```

## Differences from Task 1

| Feature | Task 1 (Router DHCP) | Task 2 (Server DHCP) |
|---------|---------------------|----------------------|
| **Server Location** | On Router R2 | Dedicated Appliance |
| **Configuration Location** | Multiple routers | Single server |
| **Scalability** | Limited | Better |
| **Resource Usage** | Router overhead | Server dedicated |
| **Admin Complexity** | Multiple configs | Single config |

## Learning Outcomes
- Understanding DHCP relay agent mechanisms
- Centralized DHCP server implementation
- IP helper addresses functionality
- Advantages of dedicated vs. router-based DHCP

---
**Completed By**: MD HASIB ULLAH KHAN ALVIE
**Student ID**: 22101371
**Course**: CSE421
**Lab Faculty**: MSMA, SRJ
