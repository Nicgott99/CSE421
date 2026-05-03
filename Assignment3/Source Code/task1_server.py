import socket

"""
TASK 1: Basic TCP Messaging Server
===================================
This server demonstrates basic TCP socket programming.

Functionality:
- Listens on port 7000 for incoming connections
- Receives client information (hostname and IP)
- Sends acknowledgment message
- Handles graceful disconnection

Message Protocol:
- Header: 64 bytes containing message length
- Body: Actual message content
- Termination: "End" message triggers connection closure
"""

ENCODING_FORMAT = "utf-8"
MESSAGE_HEADER_SIZE = 64
TERMINATION_MESSAGE = "End"

# Server configuration
server_ip_address = socket.gethostbyname(socket.gethostname())
server_port_number = 7000
server_address_tuple = (server_ip_address, server_port_number)

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address_tuple)

print("Server has started listening...")
server_socket.listen()
print(f"Server is listening on {server_ip_address}:{server_port_number}")

# Accept single client connection
client_connection, client_address = server_socket.accept()
print(f"Connected to {client_address}")

is_connected = True

while is_connected:
    # Receive message header (64 bytes containing message length)
    received_header = client_connection.recv(MESSAGE_HEADER_SIZE).decode(ENCODING_FORMAT)

    if received_header:
        # Parse message length from header
        message_length = int(received_header)
        
        # Receive message body
        received_message = client_connection.recv(message_length).decode(ENCODING_FORMAT)

        # Check for termination message
        if received_message == TERMINATION_MESSAGE:
            is_connected = False
            response = f"Goodbye! Connection with {client_address} terminated."
            client_connection.send(response.encode(ENCODING_FORMAT))
            print(f"Client disconnected: {client_address}")
        else:
            # Display received message
            print(f"Received from {client_address}: {received_message}")
            
            # Send acknowledgment
            response = "Message received successfully."
            client_connection.send(response.encode(ENCODING_FORMAT))

# Close connection
client_connection.close()
print("Server socket closed.")
