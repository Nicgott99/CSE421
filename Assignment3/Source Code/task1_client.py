import socket

"""
TASK 1: Basic TCP Messaging Client
===================================
This client demonstrates basic TCP socket programming.

Functionality:
- Connects to server on port 7000
- Sends client information (hostname and IP)
- Receives acknowledgment
- Sends termination message

Message Protocol:
- Header: 64 bytes containing message length
- Body: Actual message content
- Termination: "End" message to close connection
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
print(f"Client is trying to connect to {server_address_tuple}...")

def send_message(message_text):
    """
    Send message to server with proper header.
    
    Args:
        message_text: Message string to send
    
    Protocol:
        1. Encode message to UTF-8 bytes
        2. Calculate message length
        3. Create header with length padded to 64 bytes
        4. Send header
        5. Send message body
        6. Receive and print server response
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
    
    # Receive and display response
    response = client_socket.recv(2048).decode(ENCODING_FORMAT)
    print(f"Server Response: {response}")

# Send client information
client_info_message = f"The hostname of the client is {socket.gethostname()} and the IP address of the client is {server_ip_address}."
send_message(client_info_message)

# Send termination message
send_message(TERMINATION_MESSAGE)

# Close connection
client_socket.close()
print("Connection closed.")
