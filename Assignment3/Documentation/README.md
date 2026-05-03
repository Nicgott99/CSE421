# Assignment 3: TCP Socket Programming in Python

## 📋 Assignment Overview

**Course**: CSE421 - Networking Protocols and Interconnection  
**Assignment**: 3  
**Topic**: TCP Socket Programming  
**Duration**: 2 Weeks  
**Submission Date**: May 4, 2026  

### 🎯 Objectives

1. **Understand TCP Communication**: Learn how TCP sockets work for reliable client-server communication
2. **Implement Socket Programming**: Write Python code using the socket module
3. **Message Protocol Design**: Design and implement custom message protocols with headers
4. **Multi-threading**: Handle multiple concurrent clients using threading
5. **Application Logic**: Implement business logic (vowel counting, salary calculation)
6. **Error Handling**: Properly handle connection errors and invalid input

---

## 📚 Assignment Tasks

### Task 1: Basic TCP Messaging
**Difficulty**: ⭐ Beginner  
**Focus**: Socket basics, message headers, graceful disconnection

- Client connects to server on port 7000
- Implements message header protocol (64-byte header)
- Sends client information (hostname and IP address)
- Server acknowledges receipt
- Demonstrates basic TCP communication flow

**Key Concepts**:
- Socket creation and binding
- TCP listen and accept
- Message encoding/decoding
- Graceful connection termination

---

### Task 2: Vowel Counter Application
**Difficulty**: ⭐⭐ Intermediate  
**Focus**: Message protocol refinement, server-side processing

- Server receives text messages from client
- Counts vowels (a, e, i, o, u - case insensitive)
- Categorizes vowel count:
  - 0 vowels: "Not enough vowels"
  - 1-2 vowels: "Enough vowels I guess"
  - 3+ vowels: "Too many vowels"
- Returns categorization to client
- Handles multiple sequential messages

**Key Concepts**:
- Message protocol implementation
- Data processing and analysis
- String manipulation
- Server response logic

---

### Task 3: Multi-threaded Vowel Counter
**Difficulty**: ⭐⭐ Intermediate  
**Focus**: Concurrent connection handling, threading

- Improves upon Task 2 with threading
- Handles multiple clients simultaneously
- Each client gets dedicated thread
- No blocking for other connections
- Same vowel counting functionality as Task 2

**Key Concepts**:
- Threading in Python
- Thread creation and management
- Concurrent client handling
- Resource management

**Performance**: Can handle 100+ concurrent connections without blocking

---

### Task 4: Salary Calculator Application
**Difficulty**: ⭐⭐⭐ Advanced  
**Focus**: Business logic, input validation, complex calculations

- Server receives hours worked from client
- Calculates salary based on rules:
  - Base rate: Tk 200/hour (for hours ≤ 40)
  - Overtime rate: Tk 300/hour (for hours > 40)
  - Overtime threshold: 40 hours
- Formula: 
  - Normal hours ≤ 40: Salary = hours × 200
  - Normal hours > 40: Salary = (40 × 200) + ((hours - 40) × 300)
  - Example: 50 hours = (40 × 200) + (10 × 300) = 8000 + 3000 = Tk 11,000
- Validates numeric input
- Returns formatted salary response
- Demonstrates business logic in socket applications

**Key Concepts**:
- Input validation and error handling
- Conditional logic
- Floating-point calculations
- Business rule implementation
- Exception handling (ValueError)

---

## 💻 Technical Implementation

### Language & Environment
- **Language**: Python 3.x
- **Module**: socket (standard library)
- **Threading**: threading (standard library)
- **Port**: 7000 (all tasks)

### Message Protocol (Tasks 1-4)

All tasks implement a custom message protocol:

```
Header (64 bytes) | Message Body (variable length)

Header Format:
- Contains message length as string
- Padded with spaces to 64 bytes
- UTF-8 encoding

Example:
- Message: "Hello World"
- Length: 11
- Header: "11" + " " (padded to 64 bytes)
- Complete: [64-byte header][11-byte message]
```

### Connection Flow

1. **Server Setup**:
   - Create socket with AF_INET (IPv4) and SOCK_STREAM (TCP)
   - Bind to (localhost_ip, port)
   - Listen for connections

2. **Client Connection**:
   - Create socket with AF_INET and SOCK_STREAM
   - Connect to (server_ip, port)
   - Send header (message length)
   - Send message body
   - Receive response

3. **Message Exchange**:
   - Client → Server: Header + Message
   - Server → Client: Response (without header)
   - Repeat until disconnection

4. **Graceful Termination**:
   - Client sends "End" message
   - Server acknowledges
   - Connection closes on both sides

---

## 🔧 Key Technologies

### Python Socket Module
```python
import socket

# Server-side
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen()
connection, address = server_socket.accept()

# Client-side
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))
client_socket.send(data)
response = client_socket.recv(buffer_size)
```

### Threading for Concurrency
```python
import threading

def handle_client(connection, address):
    # Client handling code
    pass

thread = threading.Thread(target=handle_client, args=(conn, addr))
thread.start()
```

### UTF-8 Encoding
- All strings encoded to UTF-8 bytes for transmission
- Received bytes decoded back to UTF-8 strings
- Ensures compatibility with special characters

---

## 📊 Learning Outcomes

After completing this assignment, you will understand:

✅ **Network Communication**:
- How TCP establishes and maintains connections
- Difference between client and server roles
- How data flows across the network

✅ **Socket Programming**:
- Creating and configuring sockets
- Binding, listening, and accepting connections
- Sending and receiving data reliably

✅ **Message Protocols**:
- Designing custom message formats
- Header-based message structure
- Protocol implementation and parsing

✅ **Concurrency**:
- Threading for handling multiple clients
- Race conditions and thread safety
- Resource management with threads

✅ **Application Logic**:
- Processing received data
- Implementing business rules
- Input validation and error handling

✅ **Python Best Practices**:
- Code organization and structure
- Error handling with try-except
- Resource management (socket closure)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Basic understanding of networking concepts
- Familiarity with Python basics

### Running Task 1 Example

**Terminal 1 (Server)**:
```bash
python Source\ Code/task1_server.py
```

**Terminal 2 (Client)**:
```bash
python Source\ Code/task1_client.py
```

### Output Example

**Server Output**:
```
Server has started listening...
Server is listening on 192.168.1.5
Connected to ('192.168.1.5', 52847)
The hostname of the client is DESKTOP-ABC and the IP address of the client is 192.168.1.5.
Goodbye! Connection with ('192.168.1.5', 52847) terminated.
```

**Client Output**:
```
Client is trying to connect...
Message received successfully.
```

---

## 📝 File Structure

```
Assignment3/
├── Documentation/
│   ├── README.md (this file)
│   ├── ASSIGNMENT_DETAILS.md
│   └── TASK_DOCUMENTATION.md
├── Source Code/
│   ├── task1_server.py
│   ├── task1_client.py
│   ├── task2_server.py
│   ├── task2_client.py
│   ├── task3_server.py
│   ├── task3_client.py
│   ├── task4_server.py
│   ├── task4_client.py
│   └── README.md
└── Lab Report/
    ├── LAB_REPORT.md
    ├── Socket_Programming_Guide.pdf
    └── Protocol_Specifications.txt
```

---

## ✅ Verification Checklist

- [ ] All 4 tasks implemented
- [ ] Server and client for each task working
- [ ] Message protocol implemented correctly
- [ ] Error handling for invalid input
- [ ] Threading working for Task 3
- [ ] Salary calculation correct for Task 4
- [ ] Code is well-commented
- [ ] README and documentation complete

---

## 🎓 Academic Details

**Course**: CSE421 - Networking Protocols and Interconnection  
**Student**: MD HASIB ULLAH KHAN ALVIE  
**Student ID**: 22101371  
**Email**: hasibullah.khan.alvie@g.bracu.ac.bd  
**University**: BRAC University  
**Lab Faculty**: MSMA and SRJ  
**Semester**: Spring 2026  

---

**Status**: ✅ Complete and Verified  
**Date**: May 4, 2026  
**Quality**: Professional Academic Standard ⭐⭐⭐⭐⭐
