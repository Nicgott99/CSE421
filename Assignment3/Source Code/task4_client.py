import socket

"""
TASK 4: Salary Calculator Client
================================
This client sends hours worked to server for salary calculation.

Functionality:
- Connects to salary calculator server on port 7000
- Sends hours worked (numeric input)
- Receives calculated salary from server
- Repeats until "End" command

Salary Structure Implemented:
- Regular pay: Tk 200/hour (up to 40 hours)
- Overtime pay: Tk 300/hour (beyond 40 hours)

Examples:
- 30 hours → Tk 6,000
- 40 hours → Tk 8,000
- 50 hours → Tk 11,000 (8000 + 10×300)
- 60 hours → Tk 14,000 (8000 + 20×300)

Message Protocol:
- Header: 64 bytes containing message length
- Body: Hours worked (numeric string)
- Termination: "End" message to close connection

Interactive Usage:
- Run the client
- Enter hours worked (integer or decimal: 30, 45.5, etc.)
- Server responds with calculated salary
- Type "End" to disconnect
"""

ENCODING_FORMAT = "utf-8"
MESSAGE_HEADER_SIZE = 64
TERMINATION_MESSAGE = "End"

# Server configuration
server_ip_address = socket.gethostbyname(socket.gethostname())
server_port_number = 7000
server_address_tuple = (server_ip_address, server_port_number)

# Create and connect socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address_tuple)
print(f"Client connected to server at {server_address_tuple}")
print("Salary Calculator - Bangladeshi Labor Rates")
print("Regular: Tk 200/hour (up to 40 hours)")
print("Overtime: Tk 300/hour (beyond 40 hours)\\n")

def send_message(message_text):
    """
    Send hours worked to server and receive calculated salary.
    
    Args:
        message_text: String containing hours worked
    
    Protocol:
        1. Encode message to UTF-8 bytes
        2. Calculate message length
        3. Create header with length padded to 64 bytes
        4. Send header and message
        5. Receive server response with calculated salary
        6. Display formatted response
    """
    # Encode message
    encoded_message = message_text.encode(ENCODING_FORMAT)
    message_length = len(encoded_message)
    
    # Create header (message length padded to 64 bytes)
    encoded_length = str(message_length).encode(ENCODING_FORMAT)
    padded_length = encoded_length + ((b" ") * (MESSAGE_HEADER_SIZE - len(encoded_length)))
    
    # Send header and message
    client_socket.send(padded_length)
    client_socket.send(encoded_message)
    
    # Receive and display server response
    server_response = client_socket.recv(2048).decode(ENCODING_FORMAT)
    print(f"Server: {server_response}")

# Interactive loop
try:
    while True:
        user_input = input("Enter hours worked (or 'End' to disconnect): ")
        send_message(user_input)
        
        if user_input == TERMINATION_MESSAGE:
            break
except KeyboardInterrupt:
    print("\\nConnection interrupted by user.")
finally:
    # Close connection
    client_socket.close()
    print("Connection closed.")
